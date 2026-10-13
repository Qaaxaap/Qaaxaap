"""fastfetch output captured on a bare pty (zsh, TERM=xterm-kitty, truecolor).

LOGO_ROWS: the character-art logo, trimmed two rows at the top and two at the
bottom (#333333 body, #cdcd00 accents, #e5e5e5 highlights). FIELD_ROWS: from
  fastfetch -s OS:Kernel:WM:Shell -l none
None means the terminal default foreground. mkbanner.py redraws the #333333 part as
pure black and pads the shorter column with blank lines so both stay centred.
"""

LOGO_ROWS = [
    [('    .:%.    @@@@@@@@@+.       @%', '#333333', True)],
    [('   *@@@%+:  :@@@@@@@%=: .=%@@@@@@=', '#333333', True)],
    [('  :@@@@@@##@@@@@@@@@%*+%@%+@@@@@@@+', '#333333', True)],
    [('  @@#', '#333333', True), ('####', '#e5e5e5', True), ('+@@@@@@@%:', '#333333', True), ('######', '#e5e5e5', True), ('=@@@@@@@@@-', '#333333', True)],
    [(' *@%', '#333333', True), ('######', '#e5e5e5', True), ('.@@@@@#', '#333333', True), ('#########', '#e5e5e5', True), ('-@@@@@@@@#.', '#333333', True)],
    [(' %@-', '#333333', True), ('#', '#e5e5e5', True), ('.@', '#333333', True), ('=', '#e5e5e5', True), (':', '#333333', True), ('##', '#e5e5e5', True), ('+@@@@-', '#333333', True), ('###', '#e5e5e5', True), ('%@', '#333333', True), (':', '#e5e5e5', True), ('=', '#333333', True), ('###', '#e5e5e5', True), ('*@#*+=-+#:', '#333333', True)],
    [(' @@.', '#333333', True), ('#', '#e5e5e5', True), ('@@*', '#333333', True), ('=', '#e5e5e5', True), (':', '#333333', True), ('#', '#e5e5e5', True), ('-%%**-', '#333333', True), ('##', '#e5e5e5', True), ('%@@%', '#333333', True), ('*', '#e5e5e5', True), ('*', '#333333', True), ('###', '#e5e5e5', True), ('#=-', '#333333', True)],
    [(' @@-', '#333333', True), ('#', '#e5e5e5', True), ('@@@@+.-', '#333333', True), ('...', '#cdcd00', True), (':=.', '#333333', True), ('#', '#e5e5e5', True), ('%@@@@%', '#333333', True), ('###', '#e5e5e5', True), ('#-', '#333333', True)],
    [(' %@%', '#333333', True), ('##', '#e5e5e5', True), ('*#:', '#333333', True), ('.o.....o...', '#cdcd00', True), ('-%@+', '#333333', True), ('###', '#e5e5e5', True), ('#@+    -:', '#333333', True)],
    [(' +@@*', '#333333', True), ('#', '#e5e5e5', True), ('....................', '#cdcd00', True), ('+@@@@@@@@+', '#333333', True)],
    [('  @%:', '#333333', True), ('....................._:', '#cdcd00', True), ('@@@@@@@=.', '#333333', True)],
    [('  .=:', '#333333', True), ('...............__*-=`.', '#cdcd00', True), ('=@@@@@@#=.', '#333333', True)],
    [('   :+:', '#333333', True), ('....:==*__*-=`:..==-:', '#cdcd00', True), ('#@@@@@%+:', '#333333', True)],
    [('     .--=-:  ', '#333333', True), ('+..::.....-:    ', '#cdcd00', True), ('=%@*=:', '#333333', True)],
]

FIELD_ROWS = [
    [('OS', '#555555', True), (': ', '#555555', False), ('Linux From Scratch 13.0-systemd x86_64', None, False)],
    [('Kernel', '#555555', True), (': ', '#555555', False), ('Linux 7.3.0-rc1-lfs', None, False)],
    [('Window Manager', '#555555', True), (': ', '#555555', False), ('umbriel 0.1.0 (Wayland)', None, False)],
    [('Shell', '#555555', True), (': ', '#555555', False), ('zsh 5.9.2', None, False)],
]

