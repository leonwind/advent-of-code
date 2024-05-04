{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
        cargo
        rustc

        scala_3
        sbt
    ];
}
