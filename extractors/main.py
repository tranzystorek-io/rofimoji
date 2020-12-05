from extractors.blockextractor import BlockExtractor
from extractors.characterfactory import CharacterFactory
from extractors.emojiextractor import EmojiExtractor
from extractors.mathcollectionextractor import MathExtractor

if __name__ == "__main__":
    character_factory = CharacterFactory()

    EmojiExtractor().extract()
    BlockExtractor(character_factory).extract()
    MathExtractor(character_factory).extract()
