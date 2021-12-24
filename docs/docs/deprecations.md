# Deprecation Notices


## The ``nftlabs-sdk`` package

*As of November 1st, 2021*

> To be removed in `v1.0.0`

The `nftlabs-sdk` package will be deprecated at the end of 2021. We will
continue to publish versions of the package until then to give folks time
to migrate to the new `thirdweb-sdk` package.

Along with the package name being changes, the sdk type `NftlabsSdk` has also been
renamed to `ThirdwebSdk`. Please switch your usage as soon as you can as the
official `v1.0.0` release will not include the `NftlabsSdk` class.

## The `CollectionModule` class

*As of November 1st, 2021*

> To be removed in `v1.0.0`

The `collection` module (and all of its classes/types) have been renamed to `bundle` and will be deprecated at the end of 2021.

All references to `collection` module and its associated classes should be updated to `bundle` and its newely created classes.

You can find the detailed documentation for the `bundle` module [here](/api-reference/modules/bundle/)
