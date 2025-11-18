
# macOS Shortcuts Integration Guide

**Author:** RKaushik

This guide explains how to integrate the `litra-control` tool with the macOS Shortcuts app to automate control of your Litra Glow.

## Basic Shortcut: Turn Light On/Off

1.  **Open Shortcuts:** Launch the Shortcuts app on your Mac.
2.  **New Shortcut:** Click the `+` button to create a new shortcut.
3.  **Add Action:** Search for the "Run Shell Script" action and add it to your workflow.
4.  **Enter Command:** In the text box, enter the command to turn the light on:
    ```
    /usr/local/bin/litra-control on
    ```
5.  **Save Shortcut:** Give your shortcut a name, like "Litra On".

To create a shortcut to turn the light off, repeat the steps above but use the command `litra-control off`.

## Shortcut with Input: Set Brightness

You can create a shortcut that asks for input, such as a desired brightness level.

1.  **New Shortcut:** Create a new shortcut in the Shortcuts app.
2.  **Ask for Input:** Add the "Ask for Input" action. Set the `Type` to `Number` and provide a prompt, like "Enter brightness percentage (0-100)".
3.  **Run Shell Script:** Add a "Run Shell Script" action after the input action.
4.  **Pass Input to Script:** In the script box, enter the following command. The `Provided Input` variable will be replaced with the number you enter.
    ```
    /usr/local/bin/litra-control brightness "$1" -p
    ```
5.  **Save Shortcut:** Name it something like "Set Litra Brightness".

## Example Shortcuts

Here are a few more examples of how you can use `litra-control` in your shortcuts:

-   **Set Temperature:**
    ```
    /usr/local/bin/litra-control temperature 4500
    ```

-   **Toggle Light:**
    ```
    /usr/local/bin/litra-control toggle
    ```

-   **Morning Routine Shortcut:** Combine multiple actions to create a routine. For example, you could create a shortcut that turns on your Litra Glow, plays some music, and opens your calendar.

## Running Shortcuts with Siri

Once you have created your shortcuts, you can run them with Siri. For example, you can say "Hey Siri, Litra On" to run your "Litra On" shortcut.
