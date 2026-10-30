## Office Documents

Several options are available to handle standard office documents and spreadsheets: [LibreOffice](https://www.libreoffice.org/) Suite, [Calligra](https://calligra.org/) Suite, [Gnumeric](http://www.gnumeric.org/), and [AbiWord](https://www.abisource.com/). You can find these options in the OhMyDebn menu under Apps > Office.

## Xournal++

PDF files open by default in the [web browser](browser.md). If you need to annotate PDFs, then you can use the included [Xournal++](https://xournalpp.github.io/).

## Sign a PDF

To sign a PDF or fill one in, open the OhMyDebn menu and choose Apps > Office > Sign a PDF, or right-click a PDF in the file manager and choose Open With > Sign a PDF. Your PDFs still open in the [web browser](browser.md) by default.

Move the pointer to where something should go and press a key:

| Key | Places |
|-----|--------|
| `S` | Your last-used signature, under the pointer |
| `T` | A text box, ready to type in. `Shift + Enter` starts a new line; `Enter` or `Esc` finishes |
| `D` | Today's date, written the way your language and region write it |

Drag anything you've placed to move it, and drag one of its corners to make it bigger or smaller. Double-click text to change it. `Delete` removes what you've selected, the arrow keys nudge it, and `Ctrl + Z` and `Ctrl + Shift + Z` undo and redo. Press `?` in the app for all of its hotkeys.

### Adding your signature

The first time you press `S`, the app asks for a scan or photo of your signature; to add more later, click Signature and choose Add signature. You can also drop an image onto the window. Sign on plain white paper with a dark pen and take the photo in even light. The app removes the paper and keeps the ink, in its own color, so blue ink stays blue. If shadows or bits of paper are left over, slide Paper threshold toward More; if faint strokes disappear, slide it toward Less. Give the signature a name, such as your name or "Initials". You can save several, and the Signature button lists them.

### The signed copy

Press `Ctrl + S`, or click Save signed copy, to save a copy next to the original with `-signed` added to its name: signing `lease.pdf` saves `lease-signed.pdf`. The original is never changed. The signed copy keeps the original pages exactly as they were, so their text can still be selected and searched, with your signature and text laid on top.

Some PDFs carry a digital signature, which shows they haven't been changed since they were signed. Signing such a PDF here breaks that digital signature in the signed copy, so the app warns you first. The original keeps its digital signature.

### From the command line

The app's commands don't need a window, so a script or an [AI tool](ai.md) can sign a PDF with your saved signatures:

```bash
ohmydebn-pdf-sign signatures                          # your saved signatures
ohmydebn-pdf-sign add-signature "Initials" photo.jpg  # save one from a scan or photo
ohmydebn-pdf-sign pages lease.pdf                     # each page's size in points
ohmydebn-pdf-sign sign lease.pdf lease-signed.pdf --items items.json
```

`items.json` lists what to place on which page, in points from the top-left corner of the page, for example `[{"signature": "Alex", "page": 2, "x": 72, "bottom": 700, "width": 150}, {"date": true, "page": 2, "x": 300, "y": 690}]`. Run `ohmydebn-pdf-sign help items` for every option, and add `--json` to any command for output a script can read.

## Ristretto

[Ristretto](https://docs.xfce.org/apps/ristretto/start) is the default image viewer.

## GIMP

[GIMP](https://www.gimp.org/) is available as an optional installation. You can install via OhMyDebn menu (Apps > Editors). That menu option checks to see if it's installed first, so even on a new installation it will install and then run GIMP.
