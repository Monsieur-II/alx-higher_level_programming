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

	if (!*head || number < (*head)->n)
	{
		/*If it has to come at 1st position*/
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next && number > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;
	return (new);

}
