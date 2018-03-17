Summary:	Easy automated syncing between your computers and your MEGA Cloud Drive
Name:		megasync
Version:	3.6.0.0
Release:	0.1
License:	Freeware
Group:		Applications
Source0:	https://github.com/meganz/MEGAsync/archive/v%{version}_Linux/%{name}-%{version}.tar.gz
Source1:	https://github.com/meganz/sdk/archive/v3.3.3/%{name}-sdk-3.3.3.tar.gz
URL:		https://mega.nz/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	cryptopp-devel
BuildRequires:	desktop-file-utils
BuildRequires:	hicolor-icon-theme
BuildRequires:	libmediainfo-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libzen-devel
BuildRequires:	openssl-devel
BuildRequires:	sqlite3-devel
BuildRequires:	unzip
BuildRequires:	wget
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secure: Your data is encrypted end to end. Nobody can intercept it
while in storage or in transit.

Flexible: Sync any folder from your PC to any folder in the cloud.
Sync any number of folders in parallel.

Fast: Take advantage of MEGA's high-powered infrastructure and
multi-connection transfers.

Generous: Store up to 50 GB for free!

%prep
%setup -q -n MEGAsync-%{version}_Linux -a1
mv sdk-*/* src/MEGASync/mega

# use system Crypto++ header files
#rm -r src/MEGASync/mega/bindings/qt/3rdparty/include/cryptopp

%build
export DESKTOP_DESTDIR=$RPM_BUILD_ROOT%{_prefix}

cd src

./configure -i -z
qmake-qt5 DESTDIR=$RPM_BUILD_ROOT%{_bindir} THE_RPM_BUILD_ROOT=$RPM_BUILD_ROOT
lrelease-qt5  MEGASync/MEGASync.pro

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
	--add-category="Network" \
	--dir $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/megasync.desktop
%{_iconsdir}/hicolor/*/*/mega.png
