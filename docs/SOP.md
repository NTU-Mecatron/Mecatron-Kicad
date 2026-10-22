# Standard Operating Procedures
WIP

## Requesting Reviews
The following must be present for every iteration of review:
1. PDF plot of all pages of schematics, in light mode
2. PDF plot of all layers of PCB
3. Renders of the PCB
4. Bill of Materials

1. Members must create a new branch in the repo to devleop on their working version
2. Members may NOT directly merge their project into the main branch without a pull request and review (there exist rulesets in the repos to enforce this).
3. To request a review on a project, create a pull request from your working version branch to the main and request a reviewer. All files for reviews must be included in the pull request.
4. Do not close a pull request yourself. The pull request can be updated -- work in the same pull request until the changes have been merged, of which then the branch will be deleted and a new branch for the working version need to be created.


## Structure
All projects must live in the `HDK` directory,

| HDK
|> Project-Name-vX
|> Project-Name-v1

`Project-Name-vX` will always be the working version.

the project folders only get version numbers when they have been approved and sent for fabrication

fabrication directory:
Project-Name-vX -> production: Gerber (FAB-projectName-vX)
Project-Name-vX -> assembly: Bill-of-Materials (BOM-projectName-vX), Component Placement (CPC-projectName-vX)

Note that `FAB-projectName-vX` must be zipped before being sent to fabhouse


## Schematics

1. Always use hierarchical labels. Exception would be if the label is in a sheet with a parent that should not inherit this label, then use a normal label.
2. Always section off (via bounding rectangles or sheets) different functions. (ie. Input/Outputs, Power, MCU). Every section must be labeled: 2.0mm Bold Italics at the left corner of the boundary rectange

### Power Symbols
1. Power Flags are not required
2. Power symbol labels must be where the arrow is pointed (above if pointed up, left if pointed right, etc.)
3. +ve power symbols can be facing UP LEFT RIGHT
4. -ve power symbols can be facing LEFT RIGHT DOWN
5. The default ground symbol is only for "GND", the label "GND" should be removed

### Grid
All symbols, text and graphics must be on a 1.75mm, 90-degree grid

### Aesthetics
1. All text must face upright
2. There must be a wire between any 2 symbols, and there must be at least 1 unit of wire after a change in direction

### Annotation
Must be "Sort by Y", "First free after sheet number X 100"

