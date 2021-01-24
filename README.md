# Green Hills Picture Gallery


Writen by Mark Harmison, January 3, 2020.
For question or addtional features, email me at mark@octabode.com.

## Administration

This site is administer by simply uploading images files to a given directory
using FTP or other file transfer protocol.

Similarly, configuration may be modified by uploading the `config.json` file
to the images directory to modify them from the default.

## Configuration

```json
{
    "cellWidth": 240,
    "captionHeight": 20,
    "captionFont": "Arial, serif",
    "backgroundColor": "#3c3f41",
    "captionFontColor": "gainsboro",
    "refreshInterval": 60
}
```

## Security

There isn't much. This is meant to run on a Raspberry Pi or similar device
on a private network (not the Internet). Also, the information stored on this
is not private or useful to an attacker.
