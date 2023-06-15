#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);

	new->n = number;

	if (!current || number < current->n)
	{
		new->next = current;
		current->next = new;
		return (new);
	}

	while (current && current->next && number > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;
	return (new);

}
