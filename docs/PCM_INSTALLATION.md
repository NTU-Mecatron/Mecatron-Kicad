# Installing the Mecatron KiCad Library via PCM

This guide shows how to install the **Mecatron KiCad Library** using KiCad's
built-in **Plugin and Content Manager (PCM)**.

Repository URL:

```
https://ntu-mecatron.github.io/Mecatron-Kicad/pcm/repository.json
```

## 1. Add the repository to KiCad

1. Open KiCad.
2. From the KiCad project manager, open **Plugin and Content Manager**
   (the puzzle-piece icon, or **Tools → Plugin and Content Manager**).
3. Click **Manage...** (top-right of the PCM window) to open the repository
   settings.
4. Click the **+** (Add) button and paste the repository URL:

   ```
   https://ntu-mecatron.github.io/Mecatron-Kicad/pcm/repository.json
   ```

5. Click **OK** / **Save** to confirm. The new repository appears in the list.

## 2. Install the library

1. Back in the PCM window, select the **Mecatron KiCad Library** repository
   from the repository drop-down (or choose **All**).
2. Find **Mecatron KiCad Library** in the package list.
3. Click **Install**, then **Apply Pending Changes** to finish.

## 3. Verify the installation

- **Symbols**: Open the Schematic Editor → **Place Symbol** and search for
  Mecatron symbols (library tables are added automatically by PCM).
- **Footprints**: Open the PCB Editor → **Place Footprint** and search for
  Mecatron footprints.
- **3D models**: Included with the package; they resolve automatically when
  viewing footprints in the 3D viewer.

## Updating

Open the Plugin and Content Manager again — installed packages with available
updates are marked; click **Update** and **Apply Pending Changes**.

## Uninstalling

In the PCM window, select the installed **Mecatron KiCad Library** package and
click **Uninstall**, then **Apply Pending Changes**.

## Troubleshooting

- **Repository does not appear**: check the URL was pasted exactly as above,
  and that KiCad has network access.
- **Package not listed**: make sure the correct repository is selected in the
  PCM drop-down, or set it to **All**.
- **Changes not visible**: restart KiCad after installing so library tables
  are reloaded.
