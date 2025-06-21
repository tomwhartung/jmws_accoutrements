
# 2-sysctl.conf-rcsdiff_output.md

# Rcsdiff Output

Here is the one-lin change I made, along with copious comments on why I made it,
in case I go back to that project, get the error, and want to make the change again:

```
$ rcsdiff -r1.1  sysctl.conf
===================================================================
RCS file: RCS/sysctl.conf,v
retrieving revision 1.1
diff -r1.1 sysctl.conf
68a69,85
> ###################################################################
> #
> # CusTOMizations
> # --------------
> #
> ###################################################################
> #
> # 2023-05-21:
> #   Fix for "Error: ENOSPC: System limit for number of file watchers reached",
> #   Got this error trying to run React+MDBoostrap
> #   References:
> #     https://stackoverflow.com/questions/55763428/react-native-error-enospc-system-limit-for-number-of-file-watchers-reached
> #     https://stackoverflow.com/questions/65300153/error-enospc-system-limit-for-number-of-file-watchers-reached-angular
> #     https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc
> #
> fs.inotify.max_user_watches=524288
>
$
```
