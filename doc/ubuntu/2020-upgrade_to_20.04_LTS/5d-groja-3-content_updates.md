
# 5d-groja-2-content_updates.md

Continuing to update Groja.com so it is just exactly perfect.

# Content Updates and Review

## Content Updates and Review - Checklist

- [ ] Upgrade MDB to latest version: MDB 5 alpha
- [ ] Check for and remove free spiritual portrait offer, if present
    - [ ] Check the "Making Money?!?" card on the About page
- [x] Ensure social media icons link to same accounts as artsyvisions
- [ ] Set list price for a spiritual portrait to $500
    - [ ] A price of $10 appears on the `get_your_portrait` conversion page
        - http://127.0.0.1:5000/conversion/get_your_portrait`
    - [ ] Check for other occurrences of the price

- [ ] Review About page and update as appropriate
- [ ] Review entire site for anything glaring

Processes and details appear below.

## Content Updates - Process and Details

Download, install, and test.

### Upgrade MDB to Latest Version: MDB 5 Alpha

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

#### Do I Want to Do This?

I love MDB but:

- They have dropped jQuery
- They want me to use MDB CLI, which requires NPM

Looking at the site using the default version (no MDB CLI, Node, or NPM) looks almost acceptable.
Some things are just missing, and could probably be easily "resurrected."

#### Do I Want to Install Node and NPM?

Installing the default versions of node and NPM is easily done using `apt`.

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

#### Quick Start Video Notes

Watched the Quick Start Video at:

- https://mdbootstrap.com/docs/standard/getting-started/quick-start/

In it, they show how to use MDB CLI to:

- Create a starting template
  - This template looks just like the sample index.html included in the download package
- Expand the template by copying and pasting code
  - I do not need to do this for groja.com
- Publish the resultant site to mdbootstrap.com
  - I see no reason to do this

There's nothing to lose by installing MDB CLI et. al., because it's a no-brainer now that I know how,
and I probably won't even use it anyway.

#### Decision

Use apt to install Node, NPM, and MDB CLI.

- I might not use them now, but they will be useful when I do other sites

**If I have issues using them for the other sites, remember to install a newer version of node.js .**

#### Installing Node, NPM, and MDB CLI

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

Now install MDB CLI:

```
```

#### Proposed Steps:

- [x] 1. Download MDB-UI-KIT-Free-1.0.0-alpha4.zip and unpack
- [x] 2. Install Node, NPM, and MDB CLI
- [x] 3. Copy files into `static` directory
   - [x] 3.1. css/*
   - [x] 3.2. js/*
- [ ] 4. Update base.html` template to look like the downloaded version of `index.html`
- [ ] 5. Quickly test site and correct any glaring aberrations.
- [ ] 6. Keep an eye out for aberrations while performing subsequent steps


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

### Check for and Remove Free Spiritual Portrait Offer, If Present

### Check the "Making Money?!?" card on the About page

### Set list price for a spiritual portrait to $500

#### Fix the `get_your_portrait` conversion page

- http://127.0.0.1:5000/conversion/get_your_portrait`

Continued in next section!

## Review - Process and Details

### Check for Other Occurrences of the Price

### Review About Page and Update as Appropriate

### Review Entire Site for Anything Glaring

