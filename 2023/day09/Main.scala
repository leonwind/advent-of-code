object Day09 extends App {
  //val input = io.Source.fromFile("small_input.txt").getLines().toList
  val input = io.Source.fromFile("input.txt").getLines().toList

  def to_sequence(sequence: String): Seq[Int] =
    sequence.split(" ").map(_.toInt).toSeq

  val sequences = input.map(to_sequence)

  def extrapolate(sequence: Seq[Int]): Int = {
    if sequence.forall(_ == 0)
      then 0
    else
      sequence.last + extrapolate(sequence.sliding(2).map(s => s(1) - s(0)).toSeq)
  }

  println(sequences)

  val part1 = sequences.map(extrapolate).sum
  println(part1)

  val part2 = sequences.map(_.reverse).map(extrapolate).sum
  println(part2)
}