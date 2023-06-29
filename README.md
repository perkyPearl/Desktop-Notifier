# Desktop Notifier

This Python script displays desktop notifications at specific intervals using the `plyer` library. It provides various types of notifications, including random quotes and break reminders.

## Prerequisites

- Python 3.x
- `plyer` library

You can install the `plyer` library using the following command:

```
pip install plyer
```

## Usage

1. Create a file named `quotes.txt` in the same directory as the script. Each line in the file should contain a quote.

2. Run the script using the following command:

   ```
   python DesktopNotifier.py
   ```

3. The script will continuously run and display notifications based on the following triggers:

   - **Quote of the Minute**: Displays a random quote every 20 minutes.
   - **Break Time**: Displays a break reminder every 15 to 50 minutes.

4. The notifications will appear as desktop notifications on your operating system.

## Configuration

You can modify the script according to your preferences. Here are the customizable parts:

- **Quote Frequency**: By default, a new quote is displayed every 20 minutes. You can adjust this frequency by modifying the following line of code:

  ```python
  triggerQuote = time.ctime(time.time() + 60*20)
  ```

  Change `20` to the desired number of minutes between each quote.

- **Break Frequency**: By default, a break reminder is displayed every 15 to 50 minutes. You can adjust this frequency by modifying the following line of code:

  ```python
  triggerBreak = time.ctime(time.time() + 60*random.randint(15, 50))
  ```

  Change `15` and `50` to the desired range of minutes between each break reminder.

## License

This project is licensed under the [MIT License](LICENSE).

Note: The script assumes that you have an appropriate desktop notification system set up on your operating system to display the notifications. The availability and appearance of desktop notifications may vary depending on your system configuration.
