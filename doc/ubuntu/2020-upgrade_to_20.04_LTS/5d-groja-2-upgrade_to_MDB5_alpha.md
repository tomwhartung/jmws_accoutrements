
# 5d-groja-2-upgrade_to_MDB5_alpha.md

Continuing to update Groja.com so it is just exactly perfect.

# Content Updates and Review

## Update to Use MDB5 Alpha - Checklist

- [ ] Upgrade MDB to latest version: MDB 5 alpha
    - [x] 1. Download MDB-UI-KIT-Free-1.0.0-alpha4.zip and unpack
    - [x] 2. Install Node, NPM, and MDB CLI
    - [x] 3. Copy files into `static` directory
        - [x] 3.1. css/*
        - [x] 3.2. js/*
    - [x] 4. Update `base.html` template to look like the downloaded version of `index.html`
    - [x] 5. Quickly test site and correct any glaring aberrations
        - [x] 5.1. Fix the menus
    - [ ] 6. Keep an eye out for other aberrations while updating content
- [x] Ensure social media icons link to same accounts as artsyvisions
- [ ] Content Updates and Review
    - See `5d-groja-3-content_updates.md`

Processes and details appear below.

## Update to Use MDB5 Alpha - Process

Upgrade MDB to Latest Version: MDB 5 Alpha:

- Download, install, and test.

References:

- From Email:
  - https://mdbootstrap.us16.list-manage.com/track/click?u=461480655ccce528d909d3f42&id=cb39f7716f&e=a65ba5c397
- Takes me to (redirects):
  - https://mdbootstrap.com/docs/standard/?utm_campaing=MDB5&utm_medium=news&mc_cid=b025dc7b85&mc_eid=a65ba5c397
- Get Started (button):
  - https://mdbootstrap.com/docs/standard/getting-started/installation/
- From README.txt file:
  - https://mdbootstrap.com/docs/standard/
- Installation Guide:
  - https://mdbootstrap.com/docs/standard/getting-started/installation/
- Relevant Wikipedia pages:
  - https://en.wikipedia.org/wiki/Node.js
  - https://en.wikipedia.org/wiki/Npm_(software)
- Covers three options for installing Node on Ubuntu 20.04:
  - https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04
  - Using apt is the first and easiest

### MDB has Changed!

- They have dropped jQuery
- They want me to use MDB CLI, which requires NPM

#### Quick Start Video Notes

Why do they want me to install Node and NPM?

Watched the Quick Start Video at:

- https://mdbootstrap.com/docs/standard/getting-started/quick-start/

A shorter 2-minute version of the Quick Start Video is here:

- https://mdbootstrap.com/cli/

In it, they show how to use MDB CLI to:

- Create a starting template
  - This template looks just like the sample index.html included in the download package
- Expand the template by copying and pasting code
  - I do not need to do this for groja.com
- Publish the resultant site to mdbootstrap.com
  - I see no reason to do this

There's nothing to lose by installing MDB CLI et. al., because it's a no-brainer now that I know how,
and I probably won't even use it anyway.

### Installing Node, NPM, and MDB CLI

Using `apt` to install Node, NPM, and MDB CLI.

- I might not use them now, but they will be useful when I do other sites

**If there are issues using them for the other sites, remember to install a newer version of node.js .**

#### Checking Versions

Node:

- Version to be installed by apt: 10.19.0
  - 10.x: Maintenance LTS release from 2018-04-24, supported through 2021-04-01
- Latest stable version according to wikipedia: 14.6.0, released 3 days ago

The Installation Guide recommends installing "Node LTS (12.x.x recommended)."

- 12.x: Active LTS release from 2019-10-22, supported through 2022-04-01

NPM:

- Version to be installed by apt: 6.14.4
- Latest stable version according to wikipedia: 6.14.7, released 3 days ago

Installing the default versions of node and NPM is **easy** using `apt`.

**Using these versions caused a Warning when I installed `mdb-cli`.**
See below for details.

### Installation Details

Use `apt install` as follows:

```
$ apt install nodejs npm
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  gyp libc-ares2 libjs-inherits libjs-is-typedarray libjs-psl libjs-typedarray-to-buffer libnode-dev libnode64 libpython2-stdlib libpython2.7-minimal
  libpython2.7-stdlib libssl-dev libuv1-dev node-abbrev node-ajv node-ansi node-ansi-align node-ansi-regex node-ansi-styles node-ansistyles node-aproba
  node-archy node-are-we-there-yet node-asap node-asn1 node-assert-plus node-asynckit node-aws-sign2 node-aws4 node-balanced-match node-bcrypt-pbkdf node-bl
  node-bluebird node-boxen node-brace-expansion node-builtin-modules node-builtins node-cacache node-call-limit node-camelcase node-caseless node-chalk
  node-chownr node-ci-info node-cli-boxes node-cliui node-clone node-co node-color-convert node-color-name node-colors node-columnify node-combined-stream
  node-concat-map node-concat-stream node-config-chain node-configstore node-console-control-strings node-copy-concurrently node-core-util-is node-cross-spawn
  node-crypto-random-string node-cyclist node-dashdash node-debug node-decamelize node-decompress-response node-deep-extend node-defaults
  node-define-properties node-delayed-stream node-delegates node-detect-indent node-detect-newline node-dot-prop node-duplexer3 node-duplexify node-ecc-jsbn
  node-editor node-encoding node-end-of-stream node-err-code node-errno node-es6-promise node-escape-string-regexp node-execa node-extend node-extsprintf
  node-fast-deep-equal node-find-up node-flush-write-stream node-forever-agent node-form-data node-from2 node-fs-vacuum node-fs-write-stream-atomic
  node-fs.realpath node-function-bind node-gauge node-genfun node-get-caller-file node-get-stream node-getpass node-glob node-got node-graceful-fs node-gyp
  node-har-schema node-har-validator node-has-flag node-has-symbol-support-x node-has-to-string-tag-x node-has-unicode node-hosted-git-info
  node-http-signature node-iconv-lite node-iferr node-import-lazy node-imurmurhash node-inflight node-inherits node-ini node-invert-kv node-ip node-ip-regex
  node-is-npm node-is-obj node-is-object node-is-path-inside node-is-plain-obj node-is-retry-allowed node-is-stream node-is-typedarray node-isarray node-isexe
  node-isstream node-isurl node-jsbn node-json-parse-better-errors node-json-schema node-json-schema-traverse node-json-stable-stringify
  node-json-stringify-safe node-jsonify node-jsonparse node-jsonstream node-jsprim node-latest-version node-lazy-property node-lcid node-libnpx
  node-locate-path node-lockfile node-lodash node-lodash-packages node-lowercase-keys node-lru-cache node-make-dir node-mem node-mime node-mime-types
  node-mimic-fn node-mimic-response node-minimatch node-minimist node-mississippi node-mkdirp node-move-concurrently node-ms node-mute-stream node-nopt
  node-normalize-package-data node-npm-bundled node-npm-package-arg node-npm-run-path node-npmlog node-number-is-nan node-oauth-sign node-object-assign
  node-once node-opener node-os-locale node-os-tmpdir node-osenv node-p-cancelable node-p-finally node-p-is-promise node-p-limit node-p-locate node-p-timeout
  node-package-json node-parallel-transform node-path-exists node-path-is-absolute node-path-is-inside node-performance-now node-pify node-prepend-http
  node-process-nextick-args node-promise-inflight node-promise-retry node-promzard node-proto-list node-prr node-pseudomap node-psl node-pump node-pumpify
  node-punycode node-qs node-qw node-rc node-read node-read-package-json node-readable-stream node-registry-auth-token node-registry-url node-request
  node-require-directory node-require-main-filename node-resolve node-resolve-from node-retry node-rimraf node-run-queue node-safe-buffer node-semver
  node-semver-diff node-set-blocking node-sha node-shebang-command node-shebang-regex node-signal-exit node-slash node-slide node-sorted-object
  node-spdx-correct node-spdx-exceptions node-spdx-expression-parse node-spdx-license-ids node-sshpk node-ssri node-stream-each node-stream-iterate
  node-stream-shift node-strict-uri-encode node-string-decoder node-string-width node-strip-ansi node-strip-eof node-strip-json-comments node-supports-color
  node-tar node-term-size node-text-table node-through node-through2 node-timed-out node-tough-cookie node-tunnel-agent node-tweetnacl node-typedarray
  node-typedarray-to-buffer node-uid-number node-unique-filename node-unique-string node-unpipe node-uri-js node-url-parse-lax node-url-to-options
  node-util-deprecate node-uuid node-validate-npm-package-license node-validate-npm-package-name node-verror node-wcwidth.js node-which node-which-module
  node-wide-align node-widest-line node-wrap-ansi node-wrappy node-write-file-atomic node-xdg-basedir node-xtend node-y18n node-yallist node-yargs
  node-yargs-parser nodejs-doc python-pkg-resources python2 python2-minimal python2.7 python2.7-minimal
Suggested packages:
  libssl-doc python-setuptools python2-doc python-tk python2.7-doc binfmt-support
The following NEW packages will be installed:
  gyp libc-ares2 libjs-inherits libjs-is-typedarray libjs-psl libjs-typedarray-to-buffer libnode-dev libnode64 libpython2-stdlib libpython2.7-minimal
  libpython2.7-stdlib libssl-dev libuv1-dev node-abbrev node-ajv node-ansi node-ansi-align node-ansi-regex node-ansi-styles node-ansistyles node-aproba
  node-archy node-are-we-there-yet node-asap node-asn1 node-assert-plus node-asynckit node-aws-sign2 node-aws4 node-balanced-match node-bcrypt-pbkdf node-bl
  node-bluebird node-boxen node-brace-expansion node-builtin-modules node-builtins node-cacache node-call-limit node-camelcase node-caseless node-chalk
  node-chownr node-ci-info node-cli-boxes node-cliui node-clone node-co node-color-convert node-color-name node-colors node-columnify node-combined-stream
  node-concat-map node-concat-stream node-config-chain node-configstore node-console-control-strings node-copy-concurrently node-core-util-is node-cross-spawn
  node-crypto-random-string node-cyclist node-dashdash node-debug node-decamelize node-decompress-response node-deep-extend node-defaults
  node-define-properties node-delayed-stream node-delegates node-detect-indent node-detect-newline node-dot-prop node-duplexer3 node-duplexify node-ecc-jsbn
  node-editor node-encoding node-end-of-stream node-err-code node-errno node-es6-promise node-escape-string-regexp node-execa node-extend node-extsprintf
  node-fast-deep-equal node-find-up node-flush-write-stream node-forever-agent node-form-data node-from2 node-fs-vacuum node-fs-write-stream-atomic
  node-fs.realpath node-function-bind node-gauge node-genfun node-get-caller-file node-get-stream node-getpass node-glob node-got node-graceful-fs node-gyp
  node-har-schema node-har-validator node-has-flag node-has-symbol-support-x node-has-to-string-tag-x node-has-unicode node-hosted-git-info
  node-http-signature node-iconv-lite node-iferr node-import-lazy node-imurmurhash node-inflight node-inherits node-ini node-invert-kv node-ip node-ip-regex
  node-is-npm node-is-obj node-is-object node-is-path-inside node-is-plain-obj node-is-retry-allowed node-is-stream node-is-typedarray node-isarray node-isexe
  node-isstream node-isurl node-jsbn node-json-parse-better-errors node-json-schema node-json-schema-traverse node-json-stable-stringify
  node-json-stringify-safe node-jsonify node-jsonparse node-jsonstream node-jsprim node-latest-version node-lazy-property node-lcid node-libnpx
  node-locate-path node-lockfile node-lodash node-lodash-packages node-lowercase-keys node-lru-cache node-make-dir node-mem node-mime node-mime-types
  node-mimic-fn node-mimic-response node-minimatch node-minimist node-mississippi node-mkdirp node-move-concurrently node-ms node-mute-stream node-nopt
  node-normalize-package-data node-npm-bundled node-npm-package-arg node-npm-run-path node-npmlog node-number-is-nan node-oauth-sign node-object-assign
  node-once node-opener node-os-locale node-os-tmpdir node-osenv node-p-cancelable node-p-finally node-p-is-promise node-p-limit node-p-locate node-p-timeout
  node-package-json node-parallel-transform node-path-exists node-path-is-absolute node-path-is-inside node-performance-now node-pify node-prepend-http
  node-process-nextick-args node-promise-inflight node-promise-retry node-promzard node-proto-list node-prr node-pseudomap node-psl node-pump node-pumpify
  node-punycode node-qs node-qw node-rc node-read node-read-package-json node-readable-stream node-registry-auth-token node-registry-url node-request
  node-require-directory node-require-main-filename node-resolve node-resolve-from node-retry node-rimraf node-run-queue node-safe-buffer node-semver
  node-semver-diff node-set-blocking node-sha node-shebang-command node-shebang-regex node-signal-exit node-slash node-slide node-sorted-object
  node-spdx-correct node-spdx-exceptions node-spdx-expression-parse node-spdx-license-ids node-sshpk node-ssri node-stream-each node-stream-iterate
  node-stream-shift node-strict-uri-encode node-string-decoder node-string-width node-strip-ansi node-strip-eof node-strip-json-comments node-supports-color
  node-tar node-term-size node-text-table node-through node-through2 node-timed-out node-tough-cookie node-tunnel-agent node-tweetnacl node-typedarray
  node-typedarray-to-buffer node-uid-number node-unique-filename node-unique-string node-unpipe node-uri-js node-url-parse-lax node-url-to-options
  node-util-deprecate node-uuid node-validate-npm-package-license node-validate-npm-package-name node-verror node-wcwidth.js node-which node-which-module
  node-wide-align node-widest-line node-wrap-ansi node-wrappy node-write-file-atomic node-xdg-basedir node-xtend node-y18n node-yallist node-yargs
  node-yargs-parser nodejs nodejs-doc npm python-pkg-resources python2 python2-minimal python2.7 python2.7-minimal
0 upgraded, 297 newly installed, 0 to remove and 0 not upgraded.
Need to get 12.6 MB/16.5 MB of archives.
After this operation, 83.9 MB of additional disk space will be used.
Do you want to continue? [Y/n]
. . .
. . .
. . .
$ which node
/usr/bin/node
$ node --version
v10.19.0
$ which npm
/usr/bin/npm
$ npm --version
6.14.4
$
```

Wow that is a lot of packages!  Fortunately it did not take very long.

This page has the commands, which can be tricky to get from the videos.

- https://mdbootstrap.com/cli/quick-start/

Now install MDB CLI and login:

```
$ npm install -g mdb
+ mdb@0.1.0
added 2 packages from 1 contributor in 2.963s
$ which  mdb                      # Oops
$ npm install -g mdb-cli
npm WARN deprecated core-js@2.6.11: core-js@<3 is no longer maintained and not recommended for usage due to the number of issues. Please, upgrade your dependencies to the actual version of core-js@3.
/usr/local/bin/mdb -> /usr/local/lib/node_modules/mdb-cli/index.js

> core-js@2.6.11 postinstall /usr/local/lib/node_modules/mdb-cli/node_modules/core-js
> node -e "try{require('./postinstall')}catch(e){}"


$ which mdb
/usr/local/bin/mdb
$ mdb login
? Enter your MDB username tomwhartung
? Enter your MDB password **********
┌─────────┬────────┬────────────────────┐
│ (index) │ Status │      Message       │
├─────────┼────────┼────────────────────┤
│    0    │   0    │ 'Login successful' │
└─────────┴────────┴────────────────────┘
$ mdb list
┌─────────┬────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────┐
│ (index) │                  Product Name                  │                             Available                              │
├─────────┼────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────┤
│    0    │                'MDB eCommerce'                 │ 'No ( https://mdbootstrap.com/products/jquery-ecommerce-ui-kit/ )' │
│    1    │       'Material Design for Bootstrap 5'        │                               'Yes'                                │
│    2    │              'MDB PRO (Angular)'               │       'No ( https://mdbootstrap.com/products/angular-pro/ )'       │
│    3    │ 'Material Design for Bootstrap Pro (Angular)'  │     'No ( https://mdbootstrap.com/products/angular-ui-kit/ )'      │
│    4    │  'Material Design for Bootstrap 4 (Angular)'   │                               'Yes'                                │
│    5    │               'MDB PRO (React)'                │        'No ( https://mdbootstrap.com/products/react-pro/ )'        │
│    6    │  'Material Design for Bootstrap Pro (React)'   │      'No ( https://mdbootstrap.com/products/react-ui-kit/ )'       │
│    7    │   'Material Design for Bootstrap 4 (React)'    │                               'Yes'                                │
│    8    │   'Material Design for Bootstrap Pro (Vue)'    │       'No ( https://mdbootstrap.com/products/vue-ui-kit/ )'        │
│    9    │                'MDB PRO (Vue)'                 │         'No ( https://mdbootstrap.com/products/vue-pro/ )'         │
│   10    │    'Material Design for Bootstrap 4 (Vue)'     │                               'Yes'                                │
│   11    │    'MDB PRO (jQuery [standard Bootstrap])'     │      'No ( https://mdbootstrap.com/products/bootstrap-pro/ )'      │
│   12    │ 'Material Design for Bootstrap 4 Pro (jQuery)' │      'No ( https://mdbootstrap.com/products/jquery-ui-kit/ )'      │
│   13    │   'Material Design for Bootstrap 4 (jQuery)'   │                               'Yes'                                │
└─────────┴────────────────────────────────────────────────┴────────────────────────────────────────────────────────────────────┘
$
```

Notes:

- (1) The **Warning** says we are using an old version of core-js
- (2) At this time I do not plan to be using `mdb-cli`, at least not much
- (3) However, we will probably want to use this one later:

```
│    1    │       'Material Design for Bootstrap 5'        │                               'Yes'                                │
```

Possible commands we can now run include:

```
mdb init
mdb publish
```

This may be useful later, but we don't need to create a template or publish a site just now.

### Copy New Files Into `static` Directory

Copy the `css/*` and `js/* files into the `static` directory

Saving copies of the old code in: `static/css-old` and `static/js-old` for now, just in case.

### Update `base.html` Template

Update the `base.html` template to look like the downloaded version of `index.html`

Menus look totes effed up, need to fix those first.

#### Fix the Menus

Fix the nav bar in the `base.html` template.

