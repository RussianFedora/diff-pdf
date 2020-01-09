Name:           diff-pdf
Version:        0.4
Release:        1%{?dist}
Summary:        A simple tool for visually comparing two PDF files

License:        GPLv2+ and LGPLv2+
URL:            http://vslavik.github.io/diff-pdf/
Source0:        https://github.com/vslavik/diff-pdf/archive/v%{version}/diff-pdf-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  wxGTK3-devel
BuildRequires:  poppler-devel
BuildRequires:  poppler-glib-devel

%description
%{summary}.

%prep
%autosetup

%build
aclocal ${wx+-I} $wx -I admin
autoconf
automake --add-missing --copy --foreign
%configure
%make_build


%install
%make_install


%files
%license COPYING COPYING.icons
%doc AUTHORS README.md
%{_bindir}/%{name}


%changelog
* Thu Jan 09 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4-1
- Update to 0.4

* Fri Nov 15 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.3-1
- Initial release
