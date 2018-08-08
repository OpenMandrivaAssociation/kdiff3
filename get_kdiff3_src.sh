
if [ -z "$1" ]; then 
printf '%s' "Please enter kdiff3 version"
printf '%s' "You may enter a branch for the second argument to the script"
printf '%s' "The default is master"
exit
else
BASE_DIR=kdiff3-"$1"
mkdir "$BASE_DIR"
fi
if [ -z "$2" ]; then
BRANCH=master
else
BRANCH="$2"
fi
EXCLUDE="windows_installer diff_ext_for_kdiff3"
wget -qO- https://github.com/KDE/kdiff3/archive/"$BRANCH".zip | bsdtar --cd "$BASE_DIR" --strip-components 1 -xvf -
cd "$BASE_DIR" || exit;
rm -rfd ${EXCLUDE}
cd ../
tar czvf kdiff3-"$1.tar.gz" "$BASE_DIR"
rm -r "$BASE_DIR"

