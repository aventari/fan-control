package main

import (
	"fmt"
	"os"
	"strings"
)

// We use a temp file to store the "state" of the fan for this example.
const statusFile = "/tmp/fan_status.txt"

func main() {
	// Ensure we have at least one command
	if len(os.Args) < 2 {
		fmt.Println("Error: No command provided. Use 'get' or 'set'.")
		os.Exit(1)
	}

	command := os.Args[1]

	switch command {
	case "get":
		// Read the status from the file
		data, err := os.ReadFile(statusFile)
		if err != nil {
			// If file doesn't exist, assume "off"
			if os.IsNotExist(err) {
				fmt.Println("off")
				os.Exit(0)
			}
			fmt.Println("Error reading status:", err)
			os.Exit(1)
		}
		fmt.Print(string(data)) // Use Print to avoid extra newline

	case "set":
		// Ensure we have a speed to set
		if len(os.Args) < 3 {
			fmt.Println("Error: No speed provided. Use 'off', 'low', or 'high'.")
			os.Exit(1)
		}
		speed := strings.ToLower(os.Args[2])

		// Validate the input
		if speed != "off" && speed != "low" && speed != "high" {
			fmt.Println("Error: Invalid speed. Use 'off', 'low', or 'high'.")
			os.Exit(1)
		}

		// --- THIS IS WHERE YOUR RASPBERRY PI 5 LOGIC WOULD GO ---
		// For example, you would use a Go GPIO library (like periph.io)
		// to set the PWM duty cycle for the fan pin.
		// e.g., setPWM("off") -> 0% duty, setPWM("low") -> 30%, setPWM("high") -> 100%
		// --------------------------------------------------------

		// For our simulation, we just write the new speed to the file.
		err := os.WriteFile(statusFile, []byte(speed), 0644)
		if err != nil {
			fmt.Println("Error writing status:", err)
			os.Exit(1)
		}
		fmt.Println("OK") // Signal success

	default:
		fmt.Println("Error: Unknown command. Use 'get' or 'set'.")
		os.Exit(1)
	}
}