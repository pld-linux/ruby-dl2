Summary:	Dynamic Loader module for Ruby
Summary(pl):	Modu³ dynamicznego loadera dla jêzyka Ruby
Name:		ruby-dl2
%define snap	20030516
Version:	0.%{snap}.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://ttsky.net/src/%{name}-%{snap}.tar.gz
# Source0-md5:	5c99efd2f93d61bafeda0ab7b59e5629
URL:		http://w3j.ttsky.net/?ruby-dl2
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamic Loader module for Ruby.

%description -l pl
Modu³ dynamicznego loadera dla jêzyka Ruby.

%prep
%setup -q -n %{name}

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_sitearchdir}/*
%{ruby_libdir}/dl2.rb
