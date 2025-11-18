
# Example Shortcuts

This directory contains example shortcuts for controlling your Litra Glow.

## Creating Shortcuts

Since Shortcuts cannot be directly exported as files in a simple text format, follow the instructions in the [Shortcuts Guide](../../docs/SHORTCUTS_GUIDE.md) to create these shortcuts manually.

## Example 1: Turn On Light

**Command:**
```bash
/usr/local/bin/litra-control on
```

## Example 2: Turn Off Light

**Command:**
```bash
/usr/local/bin/litra-control off
```

## Example 3: Toggle Light

**Command:**
```bash
/usr/local/bin/litra-control toggle
```

## Example 4: Set Brightness to 50%

**Command:**
```bash
/usr/local/bin/litra-control brightness 50 -p
```

## Example 5: Set Temperature to Warm (3000K)

**Command:**
```bash
/usr/local/bin/litra-control temperature 3000
```

## Example 6: Set Temperature to Cool (6000K)

**Command:**
```bash
/usr/local/bin/litra-control temperature 6000
```

## Example 7: Morning Routine

Create a shortcut that:
1. Turns on the Litra Glow
2. Sets brightness to 100%
3. Sets temperature to 5000K (daylight)

**Commands:**
```bash
/usr/local/bin/litra-control on
/usr/local/bin/litra-control brightness 100 -p
/usr/local/bin/litra-control temperature 5000
```

Add each command as a separate "Run Shell Script" action in your shortcut.
