#!/bin/bash

# pg-backup.sh

# This script performs PostgreSQL database backups for the specified environment and database.

# Import the configuration file
source pg-backup-config.sh

# Create a directory with current date
CURRENT_DATETIME=$(date +"%H-%d.%m.%Y")
BACKUP_DIR="$BACKUP_PARENT_DIR/$CURRENT_DATETIME"
mkdir -p "$BACKUP_DIR"

echo "Creating backup directory: $BACKUP_DIR"

# Function to backup databases
backup_database() {
    
    echo "Backing up database: $DB_NAME"
    PGPASSWORD=$PASSWORD pg_dump -U postgres -d kediuz -f "$BACKUP_DIR/${DB_NAME}_${CURRENT_DATETIME}.sql"
    if [ $? -eq 0 ]; then
        echo "Backup of database $DB_NAME completed successfully"
    else
        echo "Backup of database $DB_NAME failed"
    fi
}

# Call the backup function
backup_database