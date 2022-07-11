class MinStack2 {
  private var stack: Stack = .init()
  private var minsWithIndex: [[Int]] = []

  func push(_ val: Int) {
    stack.push(val)
    if minsWithIndex.isEmpty || val < minsWithIndex.last![0] {
      minsWithIndex.append([val, stack.size])
    }
  }

  func pop() {
    if stack.size == minsWithIndex.last![1] {
      minsWithIndex.removeLast()
    }
    stack.pop()
  }

  func top() -> Int {
    stack.topItem
  }

  func getMin() -> Int {
    stack.isEmpty ? -1 : minsWithIndex.last![0]
  }

  var size: Int {
    return stack.size
  }
}

// KEEP MINS IN THE SAME STACK

// class MinStack {
//   private var stack: Stack = .init()
//   private var minSoFar: Int = .max

//   func push(_ val: Int) {
//     if val <= minSoFar {
//       stack.push(minSoFar)
//       minSoFar = val
//     }
//     stack.push(val)
//   }

//   func pop() -> Int {
//     var topItem = stack.pop()
//     if topItem == minSoFar {
//       minSoFar = stack.pop()
//     }
//     return topItem
//   }

//   func top() -> Int {
//     stack.topItem
//   }

//   func getMin() -> Int {
//     minSoFar
//   }
// }
