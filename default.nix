{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication rec {
  pname = "pandoc-inline-image";
  version = "0.0.1";

  src = ./.;

  propagatedBuildInputs = with pkgs; [ panflute ];

  meta = with pkgs.stdenv.lib; {
    description = "A panflute filter to embed image into html in base64 format";
    homepage = https://github.com/igsha/pandoc-inline-image;
    license = licenses.mit;
    platforms = platforms.all;
    maintainers = with maintainers; [ igsha ];
  };
}
