object Day08 extends App {
  //val input = io.Source.fromFile("small_input.txt").getLines().toList
  //val input = io.Source.fromFile("other_small.txt").getLines().toList
  val input = io.Source.fromFile("input.txt").getLines().toList

  val directions = input.head.toList
  val nodes = input.tail.tail.map({
    case s"${from} = (${left}, ${right})" => from -> (left, right)
  }).toMap

  def stepsUntilTarget(curr: String, steps: Int, target: String): Int = {
    if (curr == target)
      return steps

    val direction = directions(steps % directions.length)
    val next_node = (nodes(curr), direction) match {
      case((left, _), 'L') => left
      case((_, right), 'R') => right
    }

    stepsUntilTarget(next_node, steps + 1, target)
  }

  //println(directions)
  //println(nodes)

  val part1 = stepsUntilTarget(/* curr= */ "AAA", /* steps= */ 0, /* target= */ "ZZZ")
  println(part1)

  def stepsUntilAnyZ(curr: String, steps: Int): BigInt = {
    if (curr.takeRight(1) == "Z")
      return steps

    val direction = directions(steps % directions.length)
    val next_node = (nodes(curr), direction) match {
      case((left, _), 'L') => left
      case((_, right), 'R') => right
    }

    stepsUntilAnyZ(next_node, steps + 1)
  }

  def lcm(list: Seq[BigInt]): BigInt =
    list.foldLeft(1: BigInt) { (a, b) => b * a / Stream.iterate((a, b)) { case (x, y) => (y, x % y) }.dropWhile(_._2 != 0).head._1.abs }

  val allStepsUntilTarget = nodes.keys.filter(_.takeRight(1) == "A").map(start => stepsUntilAnyZ(start, 0)).toSeq
  val part2 = lcm(allStepsUntilTarget)
  println(part2)
}
