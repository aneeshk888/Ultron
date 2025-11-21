#!/bin/bash

# --- Configuration ---
BACKUP_DIR=".backup"
DELETION_LOG=".deletion_log"
# Add patterns here to exclude files/dirs from backup and monitoring
EXCLUDE_PATTERNS=(".git" ".vscode" ".venv" ".idea" ".backup" ".deletion_log" "__pycache__" "*.pyc" "*.pyo" "*.so" "GEMINI.md" "script.sh")

# --- Prerequisite Checks ---
for cmd in inotifywait rsync; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "Error: Required command '$cmd' is not installed." >&2
        exit 1
    fi
done

# --- Initialization ---
mkdir -p "$BACKUP_DIR"
touch "$DELETION_LOG"

# Build exclude options for rsync and inotifywait
RSYNC_EXCLUDES=()
INOTIFY_EXCLUDES=()
for pattern in "${EXCLUDE_PATTERNS[@]}"; do
    RSYNC_EXCLUDES+=(--exclude="$pattern")
    INOTIFY_EXCLUDES+=(--exclude="$pattern")
done

echo "Performing initial sync to backup directory..."
rsync -a -r --delete "${RSYNC_EXCLUDES[@]}" . "$BACKUP_DIR/"
echo "Initial sync complete. Monitoring for changes..."

# --- Main Monitoring Loop ---
inotifywait -m -r -q \
    -e create -e close_write -e delete -e moved_to -e moved_from \
    --format '%w %e %f' \
    "${INOTIFY_EXCLUDES[@]}" . | \
while read -r path events filename; do
    
    filepath="${path}${filename}"
    backup_path="${BACKUP_DIR}/${filepath#./}"

    # Ignore events in the backup directory
    if [[ "$path" == *"$BACKUP_DIR"* ]]; then
        continue
    fi
    
    # --- Event Handling ---
    if [[ "$events" == *"CREATE,ISDIR"* ]]; then
        echo "Directory created: ${filepath}. Creating in backup."
        mkdir -p "$backup_path"

    elif [[ "$events" == *"MOVED_TO,ISDIR"* ]]; then
        echo "Directory moved: ${filepath}. Creating in backup."
        # This will be handled by the MOVED_FROM and MOVED_TO of the files inside
        mkdir -p "$backup_path"

    elif [[ "$events" == *"CREATE"* || "$events" == *"CLOSE_WRITE"* || "$events" == *"MOVED_TO"* ]]; then
        echo "File created/modified/moved: ${filepath}. Updating backup."
        mkdir -p "$(dirname "$backup_path")"
        cp "$filepath" "$backup_path"
    
    elif [[ "$events" == *"DELETE,ISDIR"* ]]; then
        echo "Directory deleted: ${filepath}. Checking deletion log."
        DELETION_COUNT=$(grep -c "^${filepath}$" "$DELETION_LOG")
        if [ "$DELETION_COUNT" -lt 1 ]; then
            echo "First deletion. Restoring directory: ${filepath}."
            # The backup_path will have the trailing slash, so we need to get the parent
            rsync -a "${backup_path%/}/" "$filepath/"
            echo "${filepath}" >> "$DELETION_LOG"
        else
            echo "Not recreating ${filepath} (deleted before)."
            rm -rf "$backup_path"
        fi

    elif [[ "$events" == *"DELETE"* ]]; then
        # Check if the file is part of a directory that was just deleted and restored
        # This is a simple way to avoid restoring files in a just-restored directory
        if [ -f "$filepath" ]; then
            continue
        fi

        echo "File deleted: ${filepath}. Checking deletion log."
        DELETION_COUNT=$(grep -c "^${filepath}$" "$DELETION_LOG")
        if [ "$DELETION_COUNT" -lt 1 ]; then
            echo "First deletion. Restoring file: ${filepath}."
            mkdir -p "$(dirname "$filepath")"
            cp "$backup_path" "$filepath"
            echo "${filepath}" >> "$DELETION_LOG"
        else
            echo "Not recreating ${filepath} (deleted before)."
            rm -f "$backup_path"
        fi

    elif [[ "$events" == *"MOVED_FROM"* ]]; then
        echo "File or directory moved away: ${filepath}. Removing from backup."
        rm -rf "$backup_path"
    fi
done