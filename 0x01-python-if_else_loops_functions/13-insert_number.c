#include "lists.h"

/**
 * insert_node - Function that adds a node to a sorted list.
 * @head: Pointer to the head of the linked list.
 * @n: Data to add
 * Return: Pointer to new node.
 * Null in case of a failure.
 */

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new, *temp, *old;

	if (!head)
		return (0);
	new = malloc(sizeof(*new));
	if (!new)
		return (0);
	new->n = n;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	temp = old = *head;
	while (temp && temp->n < n)
	{
		old = temp;
		temp = temp->next;
	}
	if (old == temp)
		*head = new;
	else
		old->next = new;
	new->next = temp;
	return (new);
}
