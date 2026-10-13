<div align="center">

<img src="assets/terminal.svg" width="100%" alt="A terminal running qaaxaap's powerlevel11k prompt in ~/Projects/Qaaxaap — commands: whoami, fastfetch">

<br>
<br>

<a href="mailto:1515784026@qq.com"><img alt="email" src="https://img.shields.io/badge/-1515784026%40qq.com-f38ba8?style=flat-square&logo=gmail&logoColor=1e1e2e"></a> <a href="https://blog.qaaxaap.living"><img alt="blog" src="https://img.shields.io/badge/blog-cba6f7?style=flat-square&logo=hexo&logoColor=1e1e2e"></a> <a href="https://www.reddit.com/user/Accoiycew/"><img alt="reddit" src="https://img.shields.io/badge/reddit-Accoiycew-fab387?style=flat-square&logo=reddit&logoColor=1e1e2e"></a> <img alt="discord: Qaaxaap" src="https://img.shields.io/badge/discord-Qaaxaap-5865F2?style=flat-square&logo=discord&logoColor=1e1e2e"> <img alt="Xi'an, China" src="https://img.shields.io/badge/Xi%27an-China-94e2d5?style=flat-square&labelColor=1e1e2e">

<br>
<br>

<img alt="total stars" src="https://img.shields.io/github/stars/Qaaxaap?style=flat-square&label=total%20stars&labelColor=1e1e2e&color=f9e2af"> <img alt="followers" src="https://img.shields.io/github/followers/Qaaxaap?style=flat-square&label=followers&labelColor=1e1e2e&color=89b4fa">

</div>

Rust and C++ for the layer below the desktop: shell prompts, Wayland compositors, package tooling, and the Nix and LFS setups around them. I also work on [tuackng](https://github.com/tuackng), an OI/ICPC problem-setting toolchain, with friends.

## Projects

**[powerlevel11k](https://github.com/Qaaxaap/powerlevel11k)** is a prompt engine that continues powerlevel10k, written in Rust. It is not a shell theme: the engine owns a pty, proxies bytes untouched, and fills the header in itself. One theme therefore runs on zsh, bash, fish and pwsh. More than 80 built-in segments match p10k's, and the theme uses the KDL v2 language. Three icon tiers are available: nerdfont, compatible and ascii. Git status runs on a background thread.

```mermaid
flowchart LR
  t["terminal"] --> e["p11k engine<br/>pty host · transparent proxy"]
  e -->|spawns inside the pty| s["theme-less shell<br/>zsh · bash · fish · pwsh"]
  s -->|"renders a prompt skeleton<br/>(placeholders)"| e
  e -->|"fills in the real header"| t
```

The engine does not parse ANSI out of the pty stream and does not touch user input. The input line stays the shell's own line editor, so completion, history and vi mode keep their geometry.

I also wrote two front-ends for tuack-ng: [**Tuack-GUI**](https://github.com/tuackng/Tuack-GUI) for problem setting, and [**tuack-vscode**](https://github.com/Qaaxaap/tuack-vscode), an extension for VS Code and VSCodium that drives tuack-ng over JSON-RPC.

| Repository | What it is | Stack |
| :--- | :--- | :--- |
| [**powerlevel11k**](https://github.com/Qaaxaap/powerlevel11k) ![stars](https://img.shields.io/github/stars/Qaaxaap/powerlevel11k?style=flat-square&label=%E2%98%85&labelColor=1e1e2e&color=f9e2af) | Prompt engine after p10k: pty host, transparent proxy, multi-line header | ![Rust](https://img.shields.io/badge/-Rust-fab387?style=flat-square&logo=rust&logoColor=1e1e2e) |
| [**Tuack-GUI**](https://github.com/tuackng/Tuack-GUI) ![stars](https://img.shields.io/github/stars/tuackng/Tuack-GUI?style=flat-square&label=%E2%98%85&labelColor=1e1e2e&color=f9e2af) | Cross-platform GUI for setting OI/ICPC problems on tuack-ng: project tree, `conf.json` forms, command buttons | ![TypeScript](https://img.shields.io/badge/-TypeScript-89b4fa?style=flat-square&logo=typescript&logoColor=1e1e2e) |
| [**tuack-vscode**](https://github.com/Qaaxaap/tuack-vscode) ![stars](https://img.shields.io/github/stars/Qaaxaap/tuack-vscode?style=flat-square&label=%E2%98%85&labelColor=1e1e2e&color=f9e2af) | VS Code and VSCodium front-end for tuack-ng, driven by `tuack-ng-rpc` | ![TypeScript](https://img.shields.io/badge/-TypeScript-89b4fa?style=flat-square&logo=typescript&logoColor=1e1e2e) |
| [**d2l-learning**](https://github.com/Qaaxaap/d2l-learning) ![stars](https://img.shields.io/github/stars/Qaaxaap/d2l-learning?style=flat-square&label=%E2%98%85&labelColor=1e1e2e&color=f9e2af) | Study log for Dive into Deep Learning: notes, exercises and self-check assertions | ![Python](https://img.shields.io/badge/-Python-74c7ec?style=flat-square&logo=python&logoColor=1e1e2e) |
| [**nix-workspace**](https://github.com/Qaaxaap/nix-workspace) · [**NixOS-dots**](https://github.com/Qaaxaap/NixOS-dots) · [**vscode-dots**](https://github.com/Qaaxaap/vscode-dots) · [**klipper-dots**](https://github.com/Qaaxaap/klipper-dots) | Configuration kept in git: packages, the machine, the editor, the printer | ![Nix](https://img.shields.io/badge/-Nix-74c7ec?style=flat-square&logo=nixos&logoColor=1e1e2e) ![Klipper](https://img.shields.io/badge/-Klipper-eba0ac?style=flat-square&labelColor=1e1e2e) |
| [**qaaxaap-blog**](https://github.com/Qaaxaap/qaaxaap-blog) | The Hexo site behind [blog.qaaxaap.living](https://blog.qaaxaap.living) | ![Hexo](https://img.shields.io/badge/-Hexo-89b4fa?style=flat-square&logo=hexo&logoColor=1e1e2e) |

## Upstream patches

| Upstream | What I contributed |
| :--- | :--- |
| [**noctalia**](https://github.com/noctalia-dev/noctalia)<br><sub>noctalia-dev</sub> | Wayland desktop shell — bar font scale, PipeWire in-follow passive mode, control-center clock and tab handling, idempotent settings writes · **5 merged** |
| [**umbriel**](https://github.com/noctalia-dev/umbriel)<br><sub>noctalia-dev</sub> | scrolling/dwindle Wayland compositor — layout actions, cyclic workspace switching, per-window decoration overrides, touchpad swipe stepping, modifier-only binds, overview and umbrielfx fixes · **9 merged** |

## How I work

- Where a tool is missing or wrong, I write or patch it, in my own project or in someone else's.
- LFS on this machine, with packages from home-manager. Nix for reproducible environments: devShells most often, whole machines when needed.
- I write the code myself and use DeepSeek Harness with `deepseek-v4.1-flash` as pair programmers.
- New tools get tried early. Nix, umbriel and agentic coding stuck. Plenty of others did not.
- Contributions and co-maintainers are welcome on anything here. I review code, not people.

## Toolbox

<div align="center">

<img src="https://skillicons.dev/icons?i=rust,c,cpp,python,linux,bash,nix,lua,neovim,git,arch,vim,vscodium&theme=dark" alt="Rust, C, C++, Python, Linux, Bash, Nix, Lua, Neovim, Git, Arch, Vim, VSCodium">

<sub>Linux From Scratch #32117 · Voron v0.4408</sub>

</div>
