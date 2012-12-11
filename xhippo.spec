%define name xhippo
%define version 3.3
%define release %mkrel 9

Name: %{name}
Summary: A mp3 playlist frontend
Version: %{version}
Release: %{release}
Source: ftp://ftp.free.fr/gnu/xhippo/%{name}-%{version}.tar.bz2
Source1: %{name}-16x16.png.bz2
Source2: %{name}-32x32.png.bz2
Source3: %{name}-48x48.png.bz2
Group: Sound 
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPLv2+
BuildRequires: libgtk+-devel 
Url: http://www.gnu.org/software/xhippo/xhippo.html

%description
Xhippo is a Mp3 playlist frontend.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp xhippo.config $RPM_BUILD_ROOT%{_sysconfdir}
%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GNU xhippo
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Audio;AudioVideo;Player;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus} 
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc doc/*.* ChangeLog AUTHORS BUGS COPYING NEWS README* TODO
%config(noreplace) %{_sysconfdir}/xhippo.config
%{_bindir}/xhippo
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%_mandir/man1/*

%clean
rm -rf $RPM_BUILD_ROOT 


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.3-9mdv2010.0
+ Revision: 435132
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.3-8mdv2009.0
+ Revision: 262437
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 07 2008 Funda Wang <fundawang@mandriva.org> 3.3-5mdv2008.1
+ Revision: 163380
- fix menu entry

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 3.3-4mdv2008.1
+ Revision: 130214
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Mon Jan 08 2007 Crispin Boylan <crisb@mandriva.org> 3.3-4mdv2007.0
+ Revision: 105918
- Bump because of weird upload error
- Disable old GNOME build, XDG Menu
- Import xhippo

* Fri Jun 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.3-2mdk
- Rebuild

* Thu May 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3-1mdk
- 3.3

