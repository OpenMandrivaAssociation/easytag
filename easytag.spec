%define name       easytag
%define version 2.1
%define rel 4
%define build_plf 0
%define release %mkrel %rel
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary:      Tag editor for MP3, OGG files
Name:         %name
Version:      %version
Release:      %release
License:      GPL
URL:          http://easytag.sourceforge.net
Group:        Sound
Source:       http://prdownloads.sourceforge.net/easytag/%{name}-%{version}.tar.bz2
Source1: easytag-2.1-de.po.bz2
Patch: easytag-2.1-libid3tag.patch
Patch1: patch_21_flac_comment_fix.diff
Patch2: patch_21_rename_file_case_fix.diff
BuildRoot:    %{_tmppath}/%name-buildroot
Requires: gtk2 >= 2.4
BuildRequires: gtk2-devel >= 2.4
BuildRequires: id3lib-devel
BuildRequires: libid3tag-devel
BuildRequires: libvorbis-devel
BuildRequires: libflac-devel
BuildRequires: libwavpack-devel
%if %build_plf
BuildRequires: libmpeg4ip-devel >= 1.2
%endif
BuildRequires: autoconf2.5
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
EasyTAG is an utility for viewing and editing tags of MP3, MP2, FLAC,
Ogg Vorbis, MP4/AAC, MusePack, Wavpack and Monkey's Audio files. Its
simple and nice GTK+ interface makes tagging easier under GNU/Linux.
Features:
- View, edit, write tags of MP3, MP2 files (ID3 tag with pictures),
  FLAC files (FLAC Vorbis tag), Ogg Vorbis files (Ogg Vorbis tag),
  MP4/AAC (MP4/AAC tag), and MusePack, Wavpack, Monkey's Audio files
  (APE tag),
- Can edit more tag fields : Title, Artist, Album, Disc Album, Year,
  Track Number, Genre, Comment, Composer, Original Artist/Performer,
  Copyright, URL and Encoder name,
- Auto tagging: parse filename and directory to complete automatically
  the fields (using masks),
- Ability to rename files and directories from the tag (using masks) or by
  loading a text file,
- Process selected files of the selected directory,
- Ability to browse subdirectories,
- Recursion for tagging, removing, renaming, saving...,
- Can set a field (artist, title,...) to all other files,
- Read file header informations (bitrate, time, ...) and display them,
- Auto completion of the date if a partial is entered,
- Undo and redo last changes,
- Ability to process fields of tag and file name (convert letters into
  uppercase, downcase, ...),
- Ability to open a directory or a file with an external program,
- CDDB support using Freedb.org servers (manual and automatic search),
- A tree based browser or a view by Artist & Album,
- A list to select files,
- A playlist generator window,
- A file searching window,
- Simple and explicit interface!,
- French, German, Russian, Dutch, Hungarian, Swedish, Italian, Japanese,
  Ukrainian, Czech, Spanish, Polish, Romanian, Danish, Greek and Brazilian
  Portuguese translation languages,
- Written in C and uses GTK+ 2.4 for the GUI.
%if %build_plf
This package is in PLF as the MP4 support is violating patents.
%endif

%prep
%setup -q
bzcat %SOURCE1 > po/de.po
%patch -p1
%patch1 -p1
%patch2 -p1
aclocal
autoconf
automake

%build
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall
%{find_lang} %name
# install menu
mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):\
needs="x11"\
section="Multimedia/Sound"\
title="EasyTAG"\
longtitle="An utility for viewing/editing MP3 tags with a GTK+ GUI."\
command="easytag"\
xdg="true" \
icon="%{name}.png"
EOF
# install icons
mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
convert pixmaps/EasyTAG.xpm $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -scale 32x32 pixmaps/EasyTAG.xpm $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -scale 16x16 pixmaps/EasyTAG.xpm $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

desktop-file-install --vendor="" --add-category="GTK" \
	--add-mime-type="x-directory/normal" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-Multimedia-Sound" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%{update_menus}
%update_desktop_database

%postun
%{clean_menus}
%clean_desktop_database

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog INSTALL COPYING README TODO THANKS USERS-GUIDE
%doc doc/EasyTAG_Documentation*  doc/users_guide*
%{_bindir}/easytag
%{_mandir}/man1/easytag.1*
%{_datadir}/applications/easytag.desktop
%{_datadir}/pixmaps/*
%{_datadir}/easytag/
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
