%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		audiocd-kio
Summary:	Audio CD kio
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	840158e14b1da7c17a652e645fe4b7ed
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkcddb-devel >= %{kdeappsver}
BuildRequires:	ka5-libkcompactdisc-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcmutils-devel >= 5.24.0
BuildRequires:	kf5-kconfig-devel >= 5.24.0
BuildRequires:	kf5-kdoctools-devel >= 5.24.0
BuildRequires:	kf5-ki18n-devel >= 5.24.0
BuildRequires:	kf5-kio-devel >= 5.24.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kioslave for accessing audio CDs.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kio_audiocd.categories
%attr(755,root,root) %ghost %{_libdir}/libaudiocdplugins.so.5
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_flac.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_lame.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_vorbis.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_wav.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libkcm_audiocd.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libkio_audiocd.so
%{_datadir}/config.kcfg/audiocd_flac_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_lame_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_vorbis_encoder.kcfg
%{_datadir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/kservices5/audiocd.desktop
%{_datadir}/kservices5/audiocd.protocol
%{_datadir}/metainfo/org.kde.kio_audiocd.appdata.xml
%{_datadir}/solid/actions/solid_audiocd.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/audiocdencoder.h
%{_includedir}/audiocdplugins_export.h
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so
