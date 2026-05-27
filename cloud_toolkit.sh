#!/bin/bash
# ================================
# Cloud Engineer Toolkit v1.0
# Engineer: Saad Khan Pathan
# Phase 1 Final Project
# ================================

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}  CLOUD ENGINEER TOOLKIT v1.0  ${NC}"
echo -e "${BLUE}================================${NC}"
echo ""

# Function 1 — System check
system_check() {
    echo -e "${GREEN}SYSTEM CHECK:${NC}"
    echo "RAM Usage:"
    free -h | grep Mem
    echo "Disk Usage:"
    df -h / | grep -v Filesystem
    echo "Running Processes:"
    ps aux | wc -l
    echo ""
}

# Function 2 — Network check
network_check() {
    echo -e "${GREEN}NETWORK CHECK:${NC}"
    echo "Your IP:"
    ip addr show eth0 | grep 'inet '
    echo "Connectivity:"
    ping -c 1 google.com | grep time
    echo ""
}

# Function 3 — Security check
security_check() {
    echo -e "${GREEN}SECURITY CHECK:${NC}"
    echo "Open Ports:"
    ss -tulpn | grep LISTEN
    echo ""
}

# Function 4 — Create backup
create_backup() {
    echo -e "${GREEN}CREATING BACKUP:${NC}"
    BACKUP_DIR="backup_$(date +%Y%m%d)"
    mkdir -p $BACKUP_DIR
    cp -r ~/CloudEngineerSaad/* \
    $BACKUP_DIR/ 2>/dev/null
    echo "✅ Backup created: $BACKUP_DIR"
    echo ""
}

# Run all checks
system_check
network_check
security_check
create_backup

echo -e "${BLUE}================================${NC}"
echo -e "${GREEN}✅ All checks complete!${NC}"
echo -e "${BLUE}================================${NC}"