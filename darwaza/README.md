# Darwaza

## epub

The `epub` sub-folder contains source (html + assets + xml + opf) required to create
an epub version of this story.

An epub is simply a well (formally) structured zip file.
An excellent resource on creating one from scratch (by hand) is [here][epub-tutorial].

[epub-tutorial]: https://publicism.info/writing/ebooks/6.html

To create an epub from the source files simply `cd` into the `epub` folder and
run:

``` console
zip <filename>.epub * */* */*/* */*/*/*
```

*Note*: We have to go 4 levels deep because the assets are nested so.

## Local Preview

To preview the (unzipped) (x)html locally from the `epub` folder run
`python3.10 -m http.server -d OEBPS`

## Convert to KFX

The `mobi`/`azw3` formats do not support custom fonts properly on the Kindle.
Essentially, ligatures do not work properly.
This problem has been addressed in Amazon's propietry KFX format.
There is a mechanism to converting `epub` format to `kfx` but it is a little convoluted.
Unfortunately it does not work on Linux.

### Setup

- Install *Calibre*
- Install *Kindle Previewer version 3*
- Install Calibre's *KFX Output Plugin* (requires the *Kindle Previewer*)

### Actual Conversion

- Launch Calibre
- Open the epub version of the ebook
- Convert (individually) to KFX
- Save to disk and copy to the Kindle
