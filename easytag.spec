%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Tag editor for MP3, OGG files
Name:		easytag
Version:	2.1.8
Release:	5
License:	GPLv2+
Group:		Sound
Url:		http://projects.gnome.org/easytag/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/easytag/%{url_ver}/%{name}-%{version}.tar.xz
Source2:	easytag-2.1.6-ru.po.bz2
Patch0:		easytag-2.1.8-fix-wavpack-warning.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	id3lib-devel
BuildRequires:	libmp4v2-devel >= 1:2.0
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(speex)
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
bzcat %SOURCE2 > po/ru.po
%apply_patches

%build
%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install --vendor="" \
	--remove-mime-type="x-directory/normal" \
	--add-mime-type="inode/directory" \
	--remove-category="Editor" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc ChangeLog README TODO THANKS
%doc doc/EasyTAG_Documentation* doc/users_guide*
%{_bindir}/easytag
%{_datadir}/applications/easytag.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/easytag.1*

