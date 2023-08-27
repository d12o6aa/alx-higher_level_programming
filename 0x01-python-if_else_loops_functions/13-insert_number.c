#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *pre;
	listint_t *new;
	current = *head;
	pre = *head;
	
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
        
	new->n = number;
	new->next = NULL;
	
	if (*head == NULL)
		*head = new;
	else
	{ 
		while (current->next != NULL)
		{
			pre = current;
			if (current->n > number)
			{
				break;
			}
			current = current->next;
		}
	}
	pre->next = new;
	new->next = current;

	return new;
}
