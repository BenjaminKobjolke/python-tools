import argparse
import json
import logging
import serial
import serial.tools.list_ports

def setup_logging():
    """Sets up basic logging for the script."""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def find_arduino():
    """
    Auto-detect connected Arduino by scanning available COM ports.

    Returns:
        str: The port name if an Arduino is found, None otherwise.
    """
    ports = serial.tools.list_ports.comports()

    for port in ports:
        # Check for common Arduino identifiers in the description or manufacturer
        description = (port.description or "").lower()
        manufacturer = (port.manufacturer or "").lower()

        if any(keyword in description for keyword in ["arduino", "ch340", "ch341", "ftdi", "usb serial", "usb-serial"]):
            logging.info(f"Found Arduino on {port.device}: {port.description}")
            return port.device

        if any(keyword in manufacturer for keyword in ["arduino", "wch", "ftdi"]):
            logging.info(f"Found Arduino on {port.device}: {port.description}")
            return port.device

    return None

def list_ports():
    """List all available COM ports."""
    ports = serial.tools.list_ports.comports()

    if not ports:
        logging.info("No COM ports found.")
        return

    logging.info("Available COM ports:")
    for port in ports:
        logging.info(f"  {port.device}: {port.description}")

def send_command(port: str, baudrate: int, command: str, timeout: float):
    """
    Send a JSON command to the Arduino via serial.

    Args:
        port: The COM port to use.
        baudrate: The baud rate for serial communication.
        command: The command string to send.
        timeout: Timeout in seconds for serial operations.
    """
    setup_logging()

    # Auto-detect Arduino if port not specified
    if port is None:
        logging.info("Auto-detecting Arduino...")
        port = find_arduino()
        if port is None:
            logging.error("No Arduino found. Use --port to specify manually or --list to see available ports.")
            return False

    # Create JSON payload
    payload = json.dumps({"command": command})

    logging.info(f"Connecting to {port} at {baudrate} baud...")

    try:
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            logging.info(f"Sending: {payload}")
            ser.write((payload + "\n").encode('utf-8'))
            ser.flush()
            logging.info("Command sent successfully.")

            # Wait for and display any response
            response = ser.readline().decode('utf-8').strip()
            if response:
                logging.info(f"Response: {response}")

            return True

    except serial.SerialException as e:
        logging.error(f"Serial error: {e}")
        return False
    except Exception as e:
        logging.error(f"Error: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send JSON commands to an Arduino via serial connection."
    )
    parser.add_argument(
        "--command",
        type=str,
        help="The command to send to the Arduino (will be wrapped in JSON as {\"command\": \"<value>\"})."
    )
    parser.add_argument(
        "--port",
        type=str,
        default=None,
        help="The COM port to use (e.g., COM3). If not specified, will auto-detect Arduino."
    )
    parser.add_argument(
        "--baudrate",
        type=int,
        default=9600,
        help="The baud rate for serial communication (default: 9600)."
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=2.0,
        help="Timeout in seconds for serial operations (default: 2.0)."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available COM ports and exit."
    )

    args = parser.parse_args()

    setup_logging()

    if args.list:
        list_ports()
    elif args.command:
        send_command(args.port, args.baudrate, args.command, args.timeout)
    else:
        parser.print_help()
