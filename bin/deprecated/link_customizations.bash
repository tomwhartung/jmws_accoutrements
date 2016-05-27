#!/bin/bash
#
# link_customizations: link dirs in customizations subdir to joomla-1.5.X
# -----------------------------------------------------------------------
# On gentoo hosts, you must run this script as root.
#
hostname=$(hostname)

### if [[ $hostname == "gloria" || $hostname == "lauren" ]]; then
### ##   destination_dir="joomla"
###    echo "no need to be root on $hostname"
### else
### fi
id | grep root > /dev/null
ret_val=$?

if [ $ret_val -ne 0 ]; then
   echo "You must run this script as root."
   exit 1
fi

if [[ ! -d customizations || ! -h joomla ]]; then
   echo "Error!!"
   echo "There needs to be a customizations subdirectory and a link to the latest version of joomla here."
   echo "Get in the right directory and try again."
   exit 2
fi

#
# Ask user if we really want to do this
# -------------------------------------
#
destination_dir="joomla-1.7.3"
echo -n "Enter 'y' to link customizations to $destination_dir: "

## answer='y'
read answer

if [ "$answer" != "y" ]; then
   echo "Not linking customizations to $destination_dir: "
   exit 3
fi

## echo "answer = \"$answer\""

if [ ! -d $destination_dir ]; then
   echo "Directory \"$destination_dir\" does not exist."
   exit 5
fi

#
#  functions to create links between customizations/* and joomla/* directories
#  ===========================================================================
#
#  link_all_within_dir: link all of the files or subdirs within a directory
#  -------------------------------------------------------------------------
#
function link_all_within_dir
{
   subdir_to_link=$1
   full_dest_dir=$2
   echo
   echo "link_all_within_dir: full_dest_dir  = $full_dest_dir"
   echo "link_all_within_dir: subdir_to_link = $subdir_to_link"

   if [ ! -d ${full_dest_dir} ]; then
      echo
      echo '---> ERROR in function link_all_within_dir <---'
      echo "Unable to link ${subdir_to_link} to ${full_dest_dir}:"
      echo "Directory \"${full_dest_dir}\" does not exist!!"
      exit 7
   fi

   cd $full_dest_dir
   source_list=$(ls ${subdir_to_link}/* 2> /dev/null)
   source_count=$(echo $source_list | wc -w)
   echo "link_all_within_dir: source_list = $source_list"
   echo "linking files and/or directories to $full_dest_dir"

   if [ $source_count -gt 0 ]; then
      for source_file_or_dir in $(echo $source_list); do
         source_file_or_dir_name=$(basename $source_file_or_dir)
         echo "link_all_within_dir - loop: source_file_or_dir = $source_file_or_dir"
         echo "link_all_within_dir - loop: source_file_or_dir_name = $source_file_or_dir_name"
         ln -sf $source_file_or_dir . > /tmp/link_customizations-error.$$ 2>&1
         ret_val=$?
         if [ $ret_val -eq 0 ]; then
            echo "   File or directory linked OK: $source_file_or_dir"
         else
            echo '---> ERROR in function link_all_within_dir <---'
            echo "---> Got this error trying to link $source_file_or_dir to ${full_dest_dir}:"
            cat /tmp/link_customizations-error.$$
            echo "--------------------------------"
         fi
         rm -f /tmp/link_customizations-error.$$
      done
   else
      echo "   No subdirectories to link in $subdir_to_link"
   fi

   echo
   cd - > /dev/null
}

#
#  link_single_file_or_dir: links specified file or directory to specified destination dir
#  ---------------------------------------------------------------------------------------
#
function link_single_file_or_dir()
{
   source_file_or_dir=$1
   full_dest_dir=$2

   if [ ! -d ${full_dest_dir} ]; then
      echo
      echo '---> ERROR in function link_single_file_or_dir <---'
      echo "Unable to link ${source_file_or_dir} to ${full_dest_dir}:"
      echo "Directory \"${full_dest_dir}\" does not exist!!"
      exit 9
   fi

   cd $full_dest_dir
   file_or_dir_name=$(basename $source_file_or_dir)

   echo
   echo "link_single_file_or_dir: full_dest_dir = $full_dest_dir"
   echo "link_single_file_or_dir: source_file_or_dir = $source_file_or_dir"
   echo "link_single_file_or_dir: file_or_dir_name = $file_or_dir_name"
   error_file=/tmp/link_customizations-error.$$ 2>&1
   ln -sf $source_file_or_dir . > $error_file 2>&1
   ret_val=$?
   if [ $ret_val -eq 0 ]; then
      echo "File or directory linked OK: $source_file_or_dir"
   else
      echo
      echo '---> ERROR in function link_single_file_or_dir <---'
      echo "---> Got this error trying to link $source_file_or_dir to ${dest_dir}:"
      cat $error_file
      echo "--------------------------------"
   fi
   rm -f $error_file

   cd - > /dev/null
   return $ret_val
}

link_single_file_or_dir ../customizations/favicon.ico $destination_dir
link_single_file_or_dir ../customizations/google_adsense_script $destination_dir

### if [ -d customizations/jmsitemap ]; then
###    link_single_file_or_dir ../../customizations/jmsitemap/components/com_jmsitemap ${destination_dir}/components
###    if [ -d customizations/jmsitemap/administrator ]; then
###       link_single_file_or_dir ../../../customizations/jmsitemap/administrator/components/com_jmsitemap ${destination_dir}/administrator/components
###       link_single_file_or_dir ../../customizations/jmsitemap/language/en-GB/com_jmsitemap.ini ${destination_dir}/language/en-GB
###    fi
### fi

if [ -d customizations/joomoositestyle ]; then
   link_single_file_or_dir ../../../customizations/joomoositestyle/administrator/components/com_joomoositestyle ${destination_dir}/administrator/components
## link_single_file_or_dir ../../../customizations/joomoositestyle/administrator/modules/mod_joomoositestyle ${destination_dir}/administrator/modules
   link_single_file_or_dir ../../customizations/joomoositestyle/components/com_joomoositestyle ${destination_dir}/components
   link_single_file_or_dir ../../customizations/joomoositestyle/modules/mod_joomoositestyle ${destination_dir}/modules
   link_single_file_or_dir ../../customizations/joomoositestyle/templates/joomoositestyle ${destination_dir}/templates
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/joomoositestyle
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/joomoositestyle
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/joomoositestyle
fi

if [ -d customizations/templateparameters ]; then
   link_single_file_or_dir ../../../customizations/templateparameters/administrator/components/com_templateparameters ${destination_dir}/administrator/components
   link_single_file_or_dir ../../../customizations/templateparameters/administrator/modules/mod_templateparameters ${destination_dir}/administrator/modules
   link_single_file_or_dir ../../customizations/templateparameters/components/com_templateparameters ${destination_dir}/components
   link_single_file_or_dir ../../customizations/templateparameters/modules/mod_templateparameters ${destination_dir}/modules
   link_single_file_or_dir ../../customizations/templateparameters/templates/tmpl_templateparameters ${destination_dir}/templates
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/templateparameters
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/templateparameters
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/templateparameters
fi

if [ -d customizations/images ]; then
   if [ -d customizations/images/for_articles/ ]; then
      link_single_file_or_dir ../../customizations/images/for_articles/ ${destination_dir}/images
   fi
   if [ -d customizations/images/joomoogallery ]; then
      link_single_file_or_dir ../../customizations/images/joomoogallery  ${destination_dir}/images/
   fi
   if [ -d customizations/images/random_images ]; then
      link_single_file_or_dir ../../customizations/images/random_images  ${destination_dir}/images/
   fi
   if [ -d customizations/images/shared_images ]; then
      link_single_file_or_dir ../../customizations/images/shared_images  ${destination_dir}/images/
   fi
fi

if [ -d customizations/resume ]; then
   link_single_file_or_dir ../customizations/resume $destination_dir
fi

if [ -d customizations/tomhartung.com-original_version ]; then
   link_single_file_or_dir ../customizations/tomhartung.com-original_version $destination_dir
fi

if [ -d customizations/joomoobase ]; then
   link_single_file_or_dir ../../customizations/joomoobase/components/com_joomoobase ${destination_dir}/components
   link_single_file_or_dir ../../../customizations/joomoobase/plugins/content/joomoodebug ${destination_dir}/plugins/content/
   link_single_file_or_dir ../../../customizations/joomoobase/plugins/content/joomoosharethis ${destination_dir}/plugins/content/
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/joomoobase
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/joomoobase
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/joomoobase
fi

if [ -d customizations/joomoocomments ]; then
   link_single_file_or_dir ../../../customizations/joomoobase/components/com_joomoobase customizations/joomoocomments/components/
   link_single_file_or_dir ../../../customizations/joomoocomments/administrator/components/com_joomoocomments ${destination_dir}/administrator/components
   link_single_file_or_dir ../../customizations/joomoocomments/components/com_joomoocomments ${destination_dir}/components
   link_single_file_or_dir ../../../customizations/joomoocomments/plugins/content/joomoocomments	${destination_dir}/plugins/content
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/joomoocomments
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/joomoocomments
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/joomoocomments
fi

if [ -d customizations/joomoogallery ]; then
   link_single_file_or_dir ../../../customizations/joomoobase/components/com_joomoobase customizations/joomoogallery/components/
   link_single_file_or_dir ../../../customizations/joomoogallery/administrator/components/com_joomoogallery ${destination_dir}/administrator/components
   link_single_file_or_dir ../../customizations/joomoogallery/components/com_joomoogallery ${destination_dir}/components
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/joomoogallery
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/joomoogallery
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/joomoogallery
fi

if [ -d customizations/joomoorating ]; then
   link_single_file_or_dir ../../../customizations/joomoobase/components/com_joomoobase customizations/joomoorating/components/
   link_single_file_or_dir ../../../customizations/joomoorating/administrator/components/com_joomoorating ${destination_dir}/administrator/components
   link_single_file_or_dir ../../customizations/joomoorating/components/com_joomoorating ${destination_dir}/components
   link_single_file_or_dir ../../../customizations/joomoorating/plugins/content/joomoofixedrating ${destination_dir}/plugins/content
   link_single_file_or_dir ../../../customizations/joomoorating/plugins/content/joomoorating ${destination_dir}/plugins/content
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/joomoorating
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/joomoorating
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/joomoorating
fi

if [ -d customizations/joomoouser ]; then
   link_single_file_or_dir ../../../customizations/joomoobase/components/com_joomoobase customizations/joomoouser/components/
   link_single_file_or_dir ../../../customizations/joomoouser/administrator/components/com_joomoouser ${destination_dir}/administrator/components
   link_single_file_or_dir ../../customizations/joomoouser/components/com_joomoouser ${destination_dir}/components
   link_single_file_or_dir ../../customizations/joomoouser/modules/mod_joomoouser_login ${destination_dir}/modules
   link_single_file_or_dir ../../../customizations/joomoouser/language/en-GB/en-GB.mod_joomoouser_login.ini ${destination_dir}/language/en-GB
   link_single_file_or_dir ../../../customizations/joomoouser/language/en-GB/en-GB.mod_joomoouser_login.sys.ini ${destination_dir}/language/en-GB
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/joomoouser
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/joomoouser
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/joomoouser
fi

if [ -d customizations/groja-joomla ]; then
   link_single_file_or_dir ../../../customizations/groja-joomla/administrator/components/com_groja ${destination_dir}/administrator/components
   link_single_file_or_dir ../../customizations/groja-joomla/components/com_groja	${destination_dir}/components
   link_single_file_or_dir ../../../customizations/groja-joomla/plugins/content/grojaimagedata	 ${destination_dir}/plugins/content
   link_single_file_or_dir ../../../customizations/groja-joomla/plugins/content/grojascorescales ${destination_dir}/plugins/content
   link_single_file_or_dir ../../${destination_dir}/configuration.php customizations/groja-joomla
   link_single_file_or_dir ../../${destination_dir}/includes          customizations/groja-joomla
   link_single_file_or_dir ../../${destination_dir}/libraries         customizations/groja-joomla
fi

##
## For security reasons we are no longer supporting old versions of the site.
## Also note that running that code will just clog up the error log with notices.
## To prevent the file not found errors from showing up in the logs we link groja-phpnuke back to the joomla root directory
##
if [ -d customizations/groja-joomla ]; then
   cd ${destination_dir}
   ln -s . groja-phpnuke
fi
##
## if [ -d customizations/groja-phpnuke ]; then
##    link_single_file_or_dir ../customizations/groja-phpnuke ${destination_dir}
##    if [ ! -d ${destination_dir}/groja.com-version_2/html ]; then
##       mkdir -p ${destination_dir}/groja.com-version_2/html
##    fi
##    link_single_file_or_dir ../../customizations/index.html ${destination_dir}/groja.com-version_2
##    link_single_file_or_dir ../../../customizations/modules.php ${destination_dir}/groja.com-version_2/html
##    if [ ! -d ${destination_dir}/html ]; then
##       mkdir ${destination_dir}/html
##    fi
##    link_single_file_or_dir ../../customizations/index.html ${destination_dir}/html
##    link_single_file_or_dir ../../customizations/modules.php ${destination_dir}/html
## fi

echo
exit
