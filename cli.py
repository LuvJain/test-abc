#!/usr/bin/env python3
import click
import requests
import json
import os
from typing import Optional

# API base URL
API_URL = "http://localhost:8000"

def display_note(note):
    """Helper function to display a note in a formatted way"""
    click.echo(f"\nNote ID: {note['id']}")
    click.echo(f"Title: {note['title']}")
    click.echo(f"Content: {note['content']}")
    click.echo(f"Created: {note['created_at']}")
    click.echo(f"Updated: {note['updated_at']}")


@click.group()
def cli():
    """Notes API CLI - Manage your notes from the command line"""
    pass


@cli.command()
@click.option('--title', '-t', required=True, help='Title of the note')
@click.option('--content', '-c', required=True, help='Content of the note')
def create(title: str, content: str):
    """Create a new note"""
    try:
        response = requests.post(
            f"{API_URL}/notes/",
            json={"title": title, "content": content}
        )
        response.raise_for_status()
        note = response.json()
        click.echo("Note created successfully!")
        display_note(note)
    except requests.exceptions.RequestException as e:
        click.echo(f"Error creating note: {str(e)}")
        if hasattr(e, 'response') and e.response:
            click.echo(e.response.text)


@cli.command()
@click.option('--skip', default=0, help='Number of notes to skip')
@click.option('--limit', default=100, help='Maximum number of notes to return')
def list(skip: int, limit: int):
    """List all notes"""
    try:
        response = requests.get(
            f"{API_URL}/notes/",
            params={"skip": skip, "limit": limit}
        )
        response.raise_for_status()
        notes = response.json()

        if not notes:
            click.echo("No notes found.")
            return

        click.echo(f"\nFound {len(notes)} notes:")
        for note in notes:
            display_note(note)
            click.echo("-" * 40)
    except requests.exceptions.RequestException as e:
        click.echo(f"Error listing notes: {str(e)}")
        if hasattr(e, 'response') and e.response:
            click.echo(e.response.text)


@cli.command()
@click.argument('note_id', type=int)
def get(note_id: int):
    """Get a specific note by ID"""
    try:
        response = requests.get(f"{API_URL}/notes/{note_id}")
        response.raise_for_status()
        note = response.json()
        display_note(note)
    except requests.exceptions.RequestException as e:
        click.echo(f"Error getting note: {str(e)}")
        if hasattr(e, 'response') and e.response:
            click.echo(e.response.text)


@cli.command()
@click.argument('note_id', type=int)
@click.option('--title', '-t', help='New title for the note')
@click.option('--content', '-c', help='New content for the note')
def update(note_id: int, title: Optional[str], content: Optional[str]):
    """Update a note"""
    if not title and not content:
        click.echo("Error: You must provide at least one of --title or --content")
        return

    update_data = {}
    if title:
        update_data["title"] = title
    if content:
        update_data["content"] = content

    try:
        response = requests.patch(
            f"{API_URL}/notes/{note_id}",
            json=update_data
        )
        response.raise_for_status()
        note = response.json()
        click.echo("Note updated successfully!")
        display_note(note)
    except requests.exceptions.RequestException as e:
        click.echo(f"Error updating note: {str(e)}")
        if hasattr(e, 'response') and e.response:
            click.echo(e.response.text)


@cli.command()
@click.argument('note_id', type=int)
@click.option('--force', '-f', is_flag=True, help='Delete without confirmation')
def delete(note_id: int, force: bool):
    """Delete a note"""
    if not force:
        confirm = click.confirm(f"Are you sure you want to delete note {note_id}?")
        if not confirm:
            click.echo("Operation cancelled.")
            return

    try:
        response = requests.delete(f"{API_URL}/notes/{note_id}")
        response.raise_for_status()
        click.echo(f"Note {note_id} deleted successfully.")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error deleting note: {str(e)}")
        if hasattr(e, 'response') and e.response:
            click.echo(e.response.text)


if __name__ == '__main__':
    cli()