#!/usr/bin/perl
#
# link_customizations.pl: link customizations in $customizationsDir in cmsDuJour dir.
# -----------------------------------------------------------------------------------
#
use Cwd;
use Cwd 'chdir';

sub linkLanguageFiles( )
{
	my $extension = shift(@_);
	my $rootedLanguageFile;
	my $lnCommand;
	my $rootedSourceDir = $htdocsDir . "/" . $customizationsDir . "/" . $extension . "/language/en-GB";
	my $destinationDir = $htdocsDir . "/" . $cmsDuJour . "/language/en-GB";

	print 'Linking language files for extension ' . extension . "...\n";
	opendir LANGUAGES_DIR, $rootedSourceDir or die "Unable to open \"$rootedSourceDir\" : $!";
	@languageFiles = readdir LANGUAGES_DIR;
	closedir LANGUAGES_DIR;

	### print "rootedSourceDir: \"$rootedSourceDir\"\n";
	### print "destinationDir: \"$destinationDir\"\n";
	### print "Found the following languageFiles: @languageFiles\n";

	foreach $langFile ( @languageFiles )
	{
		$rootedLanguageFile = $rootedSourceDir . "/" . $langFile;
		if ( -f $rootedLanguageFile )
		{
			print "  linking \"$rootedLanguageFile\" to\n\t\"$destinationDir\"\n";
			$lnCommand = "cd $destinationDir; ln -fs $rootedLanguageFile . ; cd $htdocsDir";
		###	print "lnCommand: \"$lnCommand\"\n";
			system $lnCommand;
		}
	}
}

sub linkTemplateDirs( )
{
	my $extension = shift(@_);
	my $tmplDir;
	my $rootedTemplateDir;
	my $lnCommand;
	my $rootedSourceDir = $htdocsDir . "/customizations/" . $extension . "/templates";
	my $destinationDir = $htdocsDir . "/" . $cmsDuJour . "/templates";

	print 'Linking templates directories for extension ' . extension . "...\n";
	opendir TEMPLATES_DIR, $rootedSourceDir or die "Unable to open \"$rootedSourceDir\" : $!";
	@templateDirs = readdir TEMPLATES_DIR;
	closedir TEMPLATES_DIR;

	### print "rootedSourceDir: \"$rootedSourceDir\"\n";
	### print "destinationDir: \"$destinationDir\"\n";
	### print "Found the following templateDirs: @templateDirs\n";

	foreach $tmplDir ( @templateDirs )
	{
		if ( $tmplDir ne "." && $tmplDir ne ".." )
		{
			$rootedTemplateDir = $rootedSourceDir . "/" . $tmplDir;
			if ( -d $rootedTemplateDir )
			{
				print "  linking \"$rootedTemplateDir\" to\n\t\"$destinationDir\"\n";
				$lnCommand = "cd $destinationDir; ln -fs $rootedTemplateDir .; cd $htdocsDir";
			### print "lnCommand: \"$lnCommand\"\n";
				system $lnCommand;
			}
		}
	}
}

sub linkExtension( )
{
	my $extension = shift(@_);
	print "Linking files in the \"$extension\" extension...\n";

	my $githubRepoDir = $customizationsDir . '/' . $extension;
	opendir GITHUB_REPO_DIR, $githubRepoDir or die "Unable to open \"$githubRepoDir\" : $!";
	@extensionSubdirs = readdir GITHUB_REPO_DIR;
	closedir GITHUB_REPO_DIR;
	foreach $subdirectory( sort @extensionSubdirs )
	{
		if ( $subdirectory eq 'language' )
		{
			&linkLanguageFiles( $extension );
		}
		elsif ( $subdirectory eq 'templates' )
		{
			&linkTemplateDirs( $extension );
		}
		else
		{
			print "=======================================================================\n";
			print "Sorry we are not yet equipped to process directories named \"$subdirectory\" .\n";
			print "=======================================================================\n";
		}
	}
}

$customizationsDir = 'customizations';
$cmsDuJour = 'joomla';
$htdocsDir = cwd();
$exitVal = 0;

if ( -d $customizationsDir && -l $cmsDuJour )
{
	print "Found a \"$customizationsDir\" dir and a \"$cmsDuJour\" link, cool.\n";
}
else
{
	print "Expecting a \"$customizationsDir\" dir and a \"$cmsDuJour\" link, but they are not here.\n";
	print "The current directory is: \"$htdocsDir\"\n";
	print "Change to a different directory and try again.\n";
	exit 1;
}

opendir DIR_CUSTOMIZATIONS, "$customizationsDir" or die "Unable to open \"$customizationsDir\" dir. (it was just here?): $!";
@customizations = readdir DIR_CUSTOMIZATIONS;
closedir DIR_CUSTOMIZATIONS;

### print "htdocsDir: \"$htdocsDir\"\n";
### print "@customizations\n";
### $pwd = $ENV{'PWD'};
### print "pwd: \"$pwd\"\n";

foreach $extension ( @customizations )
{
	if ( $extension eq "." || $extension eq ".." )
	{
		next;
	}
	&linkExtension( $extension );
}

exit $exitVal;
