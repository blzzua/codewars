# https://www.codewars.com/kata/58259d9062cfb45e1a00006b

function map(head, f) {
  if (!head) {
    return null;
  };
  return new Node(f(head.data), map(head.next, f));
}

