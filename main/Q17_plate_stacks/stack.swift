struct Stack {
    private var items: [Int] = []

    var topItem: Int {
        return items.isEmpty ? -1 : items[items.count - 1]
    }

    var isEmpty: Bool {
        return items.isEmpty
    }

    // size needed for solution 2
    var size: Int {
        return items.count
    }

    var description: String {
        return items.description
    }

    mutating func push(_ item: Int) {
        items.append(item)
    }

    mutating func pop() -> Int {
        return items.removeLast()
    }
}
