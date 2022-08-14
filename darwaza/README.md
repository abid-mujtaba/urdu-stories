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
