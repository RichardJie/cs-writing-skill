# Contributing to Slidev Skills

Thank you for your interest in contributing to Slidev Skills! This document provides guidelines for contributing new skills or improving existing ones.

## Skill File Format

Each skill must follow this structure:

```markdown
---
name: slidev-skill-name
description: Brief description (60-150 chars). Use this skill when [use case].
---

# Skill Title

[Introduction paragraph explaining what the skill does]

## When to Use This Skill

- Use case 1
- Use case 2
- Use case 3

## Main Content

[Detailed guidance with examples]

## Examples

[Code examples and demonstrations]

## Best Practices

- Best practice 1
- Best practice 2

## Common Mistakes

- Mistake to avoid 1
- Mistake to avoid 2

## Output Format

[Template showing expected output]
```

## Naming Conventions

### Skill IDs (folder names)
- Format: `slidev-[descriptive-name]`
- All lowercase
- Use hyphens between words
- Examples: `slidev-magic-move`, `slidev-layouts`, `slidev-themes`

### Categories
- All lowercase
- Use hyphens for multi-word categories
- Current categories: `getting-started`, `content`, `code`, `visuals`, `animations`, `presentation`, `customization`, `export`

## Directory Structure

```
skills/
├── [category]/
│   └── [skill-id]/
│       └── SKILL.md
```

## Writing Guidelines

1. **Be Specific**: Provide concrete examples, not just theory
2. **Use Code Blocks**: Show actual Slidev syntax
3. **Include Output**: When relevant, show what the result looks like
4. **Keep it Practical**: Focus on real-world use cases
5. **Stay Current**: Reference the latest Slidev features (v0.50+)

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b add-skill-name`
3. Add your skill following the format above
4. Update `marketplace.json` if adding a new skill
5. Submit a pull request with a clear description

## Code of Conduct

Please be respectful and constructive in all interactions. We're here to help developers create better presentations!

## Questions?

Open an issue if you have questions about contributing.
