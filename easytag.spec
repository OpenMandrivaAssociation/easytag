%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Tag editor for MP3, OGG files
Name:		easytag
Version:	2.4.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://projects.gnome.org/easytag/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/easytag/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	id3lib-devel
BuildRequires:	libmp4v2-devel >= 1:2.0
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
Requires(post,postun):	desktop-file-utils

%description
EasyTAG is an utility for viewing and editing tags of MP3, MP2, FLAC,
Ogg Vorbis, MP4/AAC, MusePack, Wavpack, Speex and Monkey's Audio
files. Its simple and nice GTK+ interface makes tagging easier under
GNU/Linux.
Features:
- View, edit, write tags of MP3, MP2 files (ID3 tag with pictures),
  FLAC files (FLAC Vorbis tag), Ogg Vorbis files (Ogg Vorbis tag),
  MP4/AAC (MP4/AAC tag), and MusePack, Wavpack, Monkey's Audio files
  (APE tag), Speex files,
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

%prep
%setup -q 
%apply_patches

%build
%configure

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--remove-mime-type="x-directory/normal" \
	--add-mime-type="inode/directory" \
	--remove-category="Editor" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc ChangeLog README TODO THANKS
%{_bindir}/easytag
%{_datadir}/applications/easytag.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}*.svg
%{_mandir}/man1/easytag.1*
%{_libdir}/nautilus/extensions-3.0/libnautilus-easytag.so
%{_datadir}/appdata/easytag*.xml
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.*.xml
