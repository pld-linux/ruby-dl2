%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_libdir		%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define tarname dl2-ruby
Summary:	Dynamic Loader module for Ruby
Name:		ruby-dl2
%define snap	20030516
Version:	0.%{snap}.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://ttsky.net/src/%{name}-%{snap}.tar.gz
# Source0-md5:	5c99efd2f93d61bafeda0ab7b59e5629
URL:	http://w3j.ttsky.net/?ruby-dl2
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamic Loader module for Ruby.

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

make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_sitearchdir}/*
%{ruby_libdir}/dl2.rb
