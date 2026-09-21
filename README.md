<div align="center">

<img src="assets/terminal.svg" width="100%" alt="A terminal running qaaxaap's powerlevel11k prompt in ~/Projects/Qaaxaap — commands: whoami, cat ~/.philosophy, ls ~/projects">

<br>
<br>

<a href="mailto:1515784026@qq.com"><img alt="email" src="https://img.shields.io/badge/-1515784026%40qq.com-f38ba8?style=flat-square&logo=gmail&logoColor=1e1e2e"></a> <a href="https://blog.qaaxaap.living"><img alt="blog" src="https://img.shields.io/badge/blog-cba6f7?style=flat-square&logo=hexo&logoColor=1e1e2e"></a> <a href="https://www.reddit.com/user/Accoiycew/"><img alt="reddit" src="https://img.shields.io/badge/reddit-Accoiycew-fab387?style=flat-square&logo=reddit&logoColor=1e1e2e"></a> <img alt="discord: Qaaxaap" src="https://img.shields.io/badge/discord-Qaaxaap-5865F2?style=flat-square&logo=discord&logoColor=1e1e2e"> <img alt="Xi'an, China" src="https://img.shields.io/badge/Xi%27an-China-94e2d5?style=flat-square&labelColor=1e1e2e">

<br>
<br>

<img alt="total stars" src="https://img.shields.io/github/stars/Qaaxaap?style=flat-square&label=total%20stars&labelColor=1e1e2e&color=f9e2af"> <img alt="followers" src="https://img.shields.io/github/followers/Qaaxaap?style=flat-square&label=followers&labelColor=1e1e2e&color=89b4fa">

</div>

### I build my own Linux from scratch, and I write tools what I needed.

Most of that work lives one layer below the desktop: the shell prompt, the compositor, the desktop shell, and the configuration that makes a machine reproducible. Rust first; C++ when the layer underneath calls for it; Nix when the machine has to come back identical. Whenever technically feasible, I prefer to contribute upstream rather than reinvent the wheel. Some of that work is built with friends: [tuack-ng](https://github.com/tuack-ng) is our OI/ICPC problem-setting toolchain, whose GUI I wrote and maintain.

## Own work

**[powerlevel11k](https://github.com/Qaaxaap/powerlevel11k)** — a prompt engine that continues powerlevel10k, in Rust. Deliberately *not* a shell theme: the engine owns a pty, proxies bytes untouched, and fills the header in itself, so one theme runs on zsh, bash, fish and pwsh. 80+ built-in segments mirroring p10k's, a KDL v2 theme language, three icon tiers (nerdfont / compatible / ascii), and git status resolved off the prompt thread.

```mermaid
flowchart LR
  t["terminal"] --> e["p11k engine<br/>pty host · transparent proxy"]
  e -->|spawns inside the pty| s["theme-less shell<br/>zsh · bash · fish · pwsh"]
  s -->|"renders a prompt skeleton<br/>(placeholders)"| e
  e -->|"fills in the real header"| t
```

The engine never parses ANSI out of the pty stream and never touches user input.
The input line stays the shell's own line editor, so completion, history and vi
mode keep their geometry.

The other project I keep up with is [**Tuack-GUI**](https://github.com/tuack-ng/Tuack-GUI): the GUI front-end for tuack-ng's problem-setting workflow, written and maintained by me in that org.

| Repository | What it is | Stack |
| :--- | :--- | :--- |
| [**powerlevel11k**](https://github.com/Qaaxaap/powerlevel11k) ![stars](https://img.shields.io/github/stars/Qaaxaap/powerlevel11k?style=flat-square&label=%E2%98%85&labelColor=1e1e2e&color=f9e2af) | p10k's successor: pty host + transparent proxy, multi-line header, transient prompt | ![Rust](https://img.shields.io/badge/-Rust-fab387?style=flat-square&logo=rust&logoColor=1e1e2e) |
| [**Tuack-GUI**](https://github.com/tuackng/Tuack-GUI) ![stars](https://img.shields.io/github/stars/tuackng/Tuack-GUI?style=flat-square&label=%E2%98%85&labelColor=1e1e2e&color=f9e2af) | GUI front-end for OI/ICPC problem setting on top of tuack-ng: project tree, `conf.json` forms, command buttons — written and maintained by me | ![TypeScript](https://img.shields.io/badge/-TypeScript-89b4fa?style=flat-square&logo=typescript&logoColor=1e1e2e) |
| [**nix-workspace**](https://github.com/Qaaxaap/nix-workspace) | Home Manager flake workspace, reproducible end to end, and readable as a Nix entry point | ![Nix](https://img.shields.io/badge/-Nix-74c7ec?style=flat-square&logo=nixos&logoColor=1e1e2e) |
| [**NixOS-dots**](https://github.com/Qaaxaap/NixOS-dots) | My NixOS configuration | ![Nix](https://img.shields.io/badge/-Nix-74c7ec?style=flat-square&logo=nixos&logoColor=1e1e2e) |
| [**klipper-dots**](https://github.com/Qaaxaap/klipper-dots) | Klipper configuration for a Voron Trident | ![Klipper](https://img.shields.io/badge/-Klipper-eba0ac?style=flat-square&labelColor=1e1e2e) |
| [**qaaxaap-blog**](https://github.com/Qaaxaap/qaaxaap-blog) | The Hexo site behind [blog.qaaxaap.living](https://blog.qaaxaap.living) | ![Hexo](https://img.shields.io/badge/-Hexo-89b4fa?style=flat-square&logo=hexo&logoColor=1e1e2e) |

## Upstream

Patches I've sent upstream:

| Upstream | What I contributed |
| :--- | :--- |
| [**noctalia**](https://github.com/noctalia-dev/noctalia)<br><sub>noctalia-dev</sub> | Wayland desktop shell — bar font scale, PipeWire in-follow passive mode, control-center clock and tab handling, settings writes made idempotent · **5 merged** |
| [**umbriel**](https://github.com/noctalia-dev/umbriel)<br><sub>noctalia-dev</sub> | scrolling/dwindle Wayland compositor — resize from a named edge, modifier-only binds surviving an active input method, overview progress clamping · **3 merged, 4 open** |

## Toolbox

<div align="center">

<img src="https://skillicons.dev/icons?i=rust,c,cpp,python,linux,bash,nix,lua,neovim,git,arch,vim&theme=dark&perline=6" alt="Rust, C, C++, Python, Linux, Bash, Nix, Lua, Neovim, Git, Arch, Vim">

<sub>Linux From Scratch #32117 · Voron v0.4408 · Nix on the side</sub>

</div>
