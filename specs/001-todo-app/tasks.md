---

description: "Task list for Phase 1 Todo In-Memory Python Console App implementation"
---

# Tasks: Phase 1 Todo In-Memory Python Console App

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 Initialize Python project with UV and create pyproject.toml
- [X] T003 [P] Create basic file structure: src/todo_app/__init__.py
- [X] T004 [P] Create basic file structure: src/todo_app/task.py
- [X] T005 [P] Create basic file structure: src/todo_app/todo_manager.py
- [X] T006 [P] Create basic file structure: src/todo_app/cli.py
- [X] T007 [P] Create basic file structure: src/todo_app/main.py
- [X] T008 Create README.md with project overview

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Implement Task class with ID, title, description, completed status in src/todo_app/task.py
- [X] T010 [P] Implement TodoManager class with in-memory storage in src/todo_app/todo_manager.py
- [X] T011 [P] Implement basic add_task method in src/todo_app/todo_manager.py
- [X] T012 [P] Implement get_all_tasks method in src/todo_app/todo_manager.py
- [X] T013 [P] Add type hints to all classes and methods following PEP 8 standards

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to their TODO list with required title and optional description

**Independent Test**: Can be fully tested by adding tasks with different titles and descriptions, verifying they appear in the task list, and delivers the core value of task management.

### Implementation for User Story 1

- [X] T014 [P] [US1] Implement CLI command parsing for "add" command in src/todo_app/cli.py
- [X] T015 [US1] Implement prompting for title and description when adding tasks in src/todo_app/cli.py
- [X] T016 [US1] Add validation to ensure title is not empty when adding tasks in src/todo_app/cli.py
- [X] T017 [US1] Connect CLI "add" command to TodoManager.add_task method in src/todo_app/cli.py
- [X] T018 [US1] Add error handling for empty titles with user-friendly messages in src/todo_app/cli.py
- [ ] T019 [US1] Test adding tasks with different titles and descriptions to verify they appear in task list

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to view all their tasks with clear status indicators for completion

**Independent Test**: Can be fully tested by adding tasks and then viewing the list, delivering visibility into the user's tasks.

### Implementation for User Story 2

- [X] T020 [P] [US2] Implement CLI command parsing for "list" command in src/todo_app/cli.py
- [X] T021 [US2] Implement display format for listing tasks with ID, status indicator, title, and description in src/todo_app/cli.py
- [X] T022 [US2] Add clear visual indicators for completed vs incomplete tasks in src/todo_app/cli.py
- [X] T023 [US2] Handle empty task list case with appropriate message in src/todo_app/cli.py
- [X] T024 [US2] Connect CLI "list" command to TodoManager.get_all_tasks method in src/todo_app/cli.py
- [ ] T025 [US2] Test viewing task list with both completed and incomplete tasks to verify clear visual indicators

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P2)

**Goal**: Allow users to mark tasks as complete or incomplete by toggling their status

**Independent Test**: Can be fully tested by marking tasks as complete and viewing the updated status, delivering the ability to track task completion.

### Implementation for User Story 3

- [X] T026 [P] [US3] Implement CLI command parsing for "complete" command with task ID in src/todo_app/cli.py
- [X] T027 [US3] Implement toggle completion status functionality in src/todo_app/todo_manager.py
- [X] T028 [US3] Add validation to ensure task ID exists before toggling status in src/todo_app/cli.py
- [X] T029 [US3] Add error handling for invalid task IDs with user-friendly messages in src/todo_app/cli.py
- [X] T030 [US3] Connect CLI "complete" command to TodoManager.toggle_status method in src/todo_app/cli.py
- [ ] T031 [US3] Test toggling task status multiple times to verify it switches between complete/incomplete

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Existing Tasks (Priority: P2)

**Goal**: Allow users to update the title and description of existing tasks by ID

**Independent Test**: Can be fully tested by updating task details and verifying the changes persist, delivering the ability to maintain accurate task information.

### Implementation for User Story 4

- [X] T032 [P] [US4] Implement CLI command parsing for "update" command with task ID in src/todo_app/cli.py
- [X] T033 [US4] Implement prompting for new title and description when updating tasks in src/todo_app/cli.py
- [X] T034 [US4] Add validation to ensure title is not empty when updating tasks in src/todo_app/cli.py
- [X] T035 [US4] Implement update task functionality in src/todo_app/todo_manager.py
- [X] T036 [US4] Add error handling for invalid task IDs with user-friendly messages in src/todo_app/cli.py
- [X] T037 [US4] Connect CLI "update" command to TodoManager.update_task method in src/todo_app/cli.py
- [ ] T038 [US4] Test updating task details and verifying changes persist in the task list

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Allow users to delete tasks by their ID while maintaining unique and sequential IDs

**Independent Test**: Can be fully tested by deleting tasks and verifying they no longer appear in the list, delivering the ability to remove unwanted tasks.

### Implementation for User Story 5

- [X] T039 [P] [US5] Implement CLI command parsing for "delete" command with task ID in src/todo_app/cli.py
- [X] T040 [US5] Implement delete task functionality in src/todo_app/todo_manager.py
- [X] T041 [US5] Ensure IDs remain unique and sequential without reuse after deletion in src/todo_app/todo_manager.py
- [X] T042 [US5] Add error handling for invalid task IDs with user-friendly messages in src/todo_app/cli.py
- [ ] T043 [US5] Add confirmation for destructive operations (optional) in src/todo_app/cli.py
- [X] T044 [US5] Connect CLI "delete" command to TodoManager.delete_task method in src/todo_app/cli.py
- [ ] T045 [US5] Test deleting tasks and verifying they no longer appear in the task list

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T046 [P] Implement case-insensitive command matching in src/todo_app/cli.py
- [X] T047 [P] Add comprehensive input validation for all commands in src/todo_app/cli.py
- [X] T048 [P] Improve error messages for invalid commands and edge cases in src/todo_app/cli.py
- [X] T049 [P] Implement main loop with REPL-style interface in src/todo_app/main.py
- [X] T050 [P] Add quit/exit functionality to the application in src/todo_app/main.py
- [X] T051 [P] Handle edge cases: invalid commands, non-numeric IDs, very long inputs in src/todo_app/cli.py
- [X] T052 [P] Add type hints to all CLI functions in src/todo_app/cli.py
- [X] T053 [P] Update README.md with usage instructions and example commands
- [X] T054 [P] Add example commands and expected output to README.md
- [X] T055 [P] Verify all success criteria are met (SC-001 through SC-005)
- [X] T056 [P] Create demo script for hackathon judges in demo.py
- [X] T057 [P] Run final validation of all features and success criteria

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement CLI command parsing for 'add' command in src/todo_app/cli.py"
Task: "Implement prompting for title and description when adding tasks in src/todo_app/cli.py"
Task: "Add validation to ensure title is not empty when adding tasks in src/todo_app/cli.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Tasks)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test User Stories 1 & 2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 & 2 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 3 → Test independently → Deploy/Demo
4. Add User Story 4 → Test independently → Deploy/Demo
5. Add User Story 5 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence