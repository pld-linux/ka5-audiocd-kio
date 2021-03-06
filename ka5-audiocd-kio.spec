%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		audiocd-kio
Summary:	Audio CD kio
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2fc47e0e1cf7bc8b07e642220853ac4a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkcddb-devel >= %{kdeappsver}
BuildRequires:	ka5-libkcompactdisc-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libaudiocdplugins.so.5
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_flac.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_lame.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_vorbis.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_wav.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_audiocd.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/audiocd.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libaudiocd_encoder_opus.so
%{_datadir}/config.kcfg/audiocd_flac_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_lame_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_opus_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_vorbis_encoder.kcfg
%{_datadir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/kservices5/audiocd.desktop
%{_datadir}/kservices5/audiocd.protocol
%{_datadir}/solid/actions/solid_audiocd.desktop
%{_datadir}/qlogging-categories5/kio_audiocd.categories
%{_datadir}/metainfo/org.kde.kio_audiocd.metainfo.xml
%{_datadir}/qlogging-categories5/kio_audiocd.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/audiocdencoder.h
%{_includedir}/audiocdplugins_export.h
%{_libdir}/libaudiocdplugins.so
