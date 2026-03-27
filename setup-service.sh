#!/bin/bash
# Setup script for SGLang systemd service

echo "Installing SGLang systemd service..."
echo

# Copy service file to systemd directory
sudo cp /home/tchen19/LLM/sglang.service /etc/systemd/system/

# Reload systemd daemon
sudo systemctl daemon-reload

echo "✓ Service file installed"
echo
echo "Available commands:"
echo "  Start service:    sudo systemctl start sglang"
echo "  Stop service:     sudo systemctl stop sglang"
echo "  Restart service:  sudo systemctl restart sglang"
echo "  Status:           sudo systemctl status sglang"
echo "  Enable on boot:   sudo systemctl enable sglang"
echo "  View logs:        sudo journalctl -u sglang -f"
echo
echo "To enable autostart on reboot:"
echo "  sudo systemctl enable sglang"
echo
echo "To start the service now:"
echo "  sudo systemctl start sglang"
echo
