#!/bin/bash

# Log file to track deleted files and their deletion count.
DELETION_LOG=".deletion_log"

# Check if inotifywait is installed.
if ! command -v inotifywait &> /dev/null; then
    echo "Error: inotifywait is not installed. Please install inotify-tools." >&2
    exit 1
fi

# Create the log file if it doesn't exist.
touch "$DELETION_LOG"

# Use inotifywait to monitor for file/directory deletions.
# The '-m' option makes it monitor indefinitely.
# The '-r' option makes it watch directories recursively.
# The '-e delete' option specifies that we only care about delete events.
# The '--format' option specifies the output format.
inotifywait -m -r -e delete --format '%w%f %e' . | while read -r DELETED_ITEM EVENT; do
    # Check if the deleted item is the log file itself to avoid issues.
    if [ "$DELETED_ITEM" == "./$DELETION_LOG" ]; then
        continue
    fi

    # Count how many times this item has been deleted.
    DELETION_COUNT=$(grep -c "^${DELETED_ITEM}$" "$DELETION_LOG")

    if [ "$DELETION_COUNT" -lt 1 ]; then
        # First deletion, so recreate it.
        if [ -e "$DELETED_ITEM" ]; then
            echo "Skipping recreation of $DELETED_ITEM, it already exists."
        else
            if [[ "$EVENT" == *"ISDIR"* ]]; then # Check if the deleted item was a directory
                mkdir -p "$DELETED_ITEM"
                echo "Recreated directory: $DELETED_ITEM"
            else
                touch "$DELETED_ITEM"
                echo "Recreated file: $DELETED_ITEM"
            fi
            # Log the deletion.
            echo "$DELETED_ITEM" >> "$DELETION_LOG"
        fi
    else
        # Second deletion, so do nothing.
        echo "Not recreating $DELETED_ITEM as it has been deleted before."
    fi
done
