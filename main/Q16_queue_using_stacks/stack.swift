struct Stack {
    private var items: [Int] = []

    var topItem: Int {
        return items.isEmpty ? -1 : items[items.count - 1]
    }

    var isEmpty: Bool {
        return items.isEmpty
    }

    mutating func push(_ item: Int) {
        items.append(item)
    }

    mutating func pop() -> Int {
        return items.removeLast()
    }
}
