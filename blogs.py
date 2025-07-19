from fasthtml.common import *

BLOG_POSTS = {
    "fury-road-redemption": {
        "title": "The Redemption Arc: Mad Max Fury Road",
        "date": "August 11, 2024",
        "snippet": "I watched Fury Road Black and Chrome edition recently, after going to "
                "see the new Furiosa multiple times, and loving it.",
        "content": Div(
            P(
                "I watched Fury Road Black and Chrome edition recently, after going to "
                "see the new Furiosa multiple times, and loving it."
            ),
            P(
                "Director George Miller said of his film that he thought Black and Chrome "
                "was the definitive edition of Fury Road, and his favorite edition, and I "
                "have to agree. I've seen the movie more times than I can count, but the "
                "first time I watched B&C I felt chills down my spine and the characters' "
                "emotional journey hit me in a way that I totally wasn't expecting."
            ),
            P(
                "When they escaped into the sand storm, when Angharad goes under the "
                "wheels, when Furiosa discovers that the 'Green Place' has been corrupted by "
                "the nuclear-fallout induced rot gripping the planet, the affect was so powerful "
                "each time that I couldn't help but to pause the movie and let the emotional "
                "turbulence wash over me."
            ),
            P(
                "How is it that a black and white color grading could make the movie so "
                "much more powerful? Well, it's easy to imagine the reverse, a garish "
                "over-saturated color grading so bad that it made the movie uninteresting "
                "or unwatchable. I think that taking the color out reduces the cognitive "
                "load of a movie that is already so densely packed with symbolism and "
                "action that you can actually start to process the powerful story and the "
                "journeys of the characters in real, or closer to real time."
            ),
            P(
                "What I realized this time around, is that the basic structure of the "
                "story is a deeply archetypal and ancient story structure: facing a "
                "crisis of identity, of morals, of being stretched to the limit, the "
                "antagonist triggers a regression to the past, to childhood, the 'Green "
                "Place'. This is followed by the tragic realization that the world of the "
                "child, the coping mechanisms, the attitude to the world at the time of "
                "childhood, are no longer fruitful or in fact they are now rotten. Which "
                "then prompts a decision-- whether to remain in the rotten world of "
                "childhood, doomed, and dying from lack of new inputs, or to abandon "
                "everything and to attempt to be reborn in the unknown."
            ),
            P(
                "Furiosa correctly identifies that she cannot simply stay in the "
                "corrupted green place with her old tribe. She knows that the only path "
                "forward is renewal, and she decides to ride into the unknown, a brave "
                "choice, but one that seems doomed to an almost certain death riding into "
                "an impossible stretch of wasteland."
            ),
            P(
                "Max, the seemingly immortal 'Wandering Jew' of the Australian "
                "wastelands, who has the appearance of a man in his forties, but somehow "
                "was police before the world fell apart more than forty years ago, steps "
                "in with his archaic wisdom, seeing a third option and a true opportunity "
                "for Furiosa's redemption."
            ),
            P(
                "He suggests that instead of abandoning the world as they know it, they "
                "seek to return directly to the center of Furiosa's pathos, to tear down "
                "the corrupted, bloated emperor, and free the land from his tyrannical, "
                "pathological, and cruel rule."
            ),
            P(
                "In psychological terms, this is the midlife crisis, when one has grown "
                "exhausted under the harsh conditions imposed on one's self to thrive in "
                "the world, and the inauthenticity required to interface with the "
                "collective constructs of society, and the only way forward is to either "
                "abandon everything, or to overthrow one's cruel reason and to "
                "renegotiate a contract with one's self and the world. The renegotiation "
                "is clearly the more heroic path, but it requires the most psychological "
                "depth and maturity as well."
            ),
            P(
                "The renegotiation is not without sacrifices. Old and new friends alike "
                "are lost as the path back to the center is tread. But if successful, a "
                "new font of creativity, a well of fresh water, can be released that can "
                "power the second half of life, as can be seen when the aqueducts are "
                "released at the end of the movie."
            ),
        ),
    },
    "format-dataset": {
        "title": "Formatting Conversation Dataset for Fine-tuning: A Tool for Preparing Your Data",
        "date": "July 14, 2024",
        "snippet": "You've transcribed, diarized, and maybe even gone to some lengths to improve the",
        "content": Div(
            P(
                "You've transcribed, diarized, and maybe even gone to some lengths to improve the "
                "quality of the diarization further with an LLM. So now you're ready to finetune a "
                "model with your data, right? Not quite."
            ),
            P(
                "You still need to put the information in a format suited to fine-tuning your model. "
                "OpenAI has a guide to this, but in short, you need to turn your conversational data "
                "into something that looks like this:"
            ),
            Pre(
                Code(
                    '{"messages": [{"role": "system", "content": "Marv is a factual chatbot '
                    'that is also sarcastic."}, {"role": "user", "content": "What\'s the capital '
                    'of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn\'t '
                    'know that already."}]}'
                )
            ),
            Pre(
                Code(
                    '{"messages": [{"role": "system", "content": "Marv is a factual chatbot '
                    'that is also sarcastic."}, {"role": "user", "content": "Who wrote \'Romeo and '
                    'Juliet\'?"}, {"role": "assistant", "content": "Oh, just some guy named William '
                    'Shakespeare. Ever heard of him?"}]}'
                )
            ),
            Pre(
                Code(
                    '{"messages": [{"role": "system", "content": "Marv is a factual chatbot '
                    'that is also sarcastic."}, {"role": "user", "content": "How far is the Moon '
                    'from Earth?"}, {"role": "assistant", "content": "Around 384,400 kilometers. '
                    'Give or take a few, like that really matters."}]}'
                )
            ),
            P(
                "Obviously, I need to do this too! So I made a tool that works nicely for my usecase."
            ),
            P("Here are the docs:"),
            A(
                "russedavid.github.io/format_conversation_dataset/",
                href="https://russedavid.github.io/format_conversation_dataset/",
            ),
            P("and here's the github repo:"),
            A(
                "github.com/russedavid/format_conversation_dataset",
                href="https://github.com/russedavid/format_conversation_dataset",
            ),
            P(
                "The way my diarized transcription is outputted, I have a speaker on each line. Since I'm "
                "trying to get the model to emulate one of the speakers only, my formatter will take as an "
                "input a 2 digit string representation of the speaker “number”, like “02” and use that to "
                "designate that speaker as the ‘assistant’ for formatting purposes. Then, all of the other "
                "speakers, their label and their content will be concat'ed together till the next assistant line."
            ),
            P(
                "There's an optional context parameter as well if you want to provide a system input at the "
                "beginning helping to explain the assistant's role in the conversation."
            ),
        ),
    },
    "improve-diarization-claude": {
        "title": "Improving Diarization with LLMs: A Journey through nbdev and Claude",
        "date": "July 6, 2024",
        "snippet": "If you enjoy programming Python in notebooks (which I do, despite the ",

        "content": Div(
            P(
                "If you enjoy programming Python in notebooks (which I do, despite the "
                "potential complexities when creating artifacts) and appreciate good, "
                "“automatically” generated documentation hosted on a website, you might "
                "find nbdev intriguing."
            ),
            P("For more information, visit:"),
            A("nbdev.fast.ai", href="https://nbdev.fast.ai/"),
            P(
                "For the small price of adding various annotations to your notebook to "
                "export only the proper module while simultaneously generating "
                "documentation, you gain commands that will publish the exported module "
                "to PyPI and Conda, along with a GitHub Pages site hosting your "
                "documentation in a pleasant format. There's much more to explore in "
                "their documentation:"
            ),
            A(
                "nbdev.fast.ai/getting_started.html",
                href="https://nbdev.fast.ai/getting_started.html",
            ),
            P(
                "I mention this because I recently had the opportunity to try improving "
                "diarization with LLMs (credit to this paper for the idea) while also "
                "satisfying my curiosity about nbdev. This project aligned nicely with my "
                "recent enjoyment of Claudette, which works great in a notebook and serves "
                "as an excellent replacement for Claude's website UI when I encounter throttling issues."
            ),
            H3("Improving Diarization with LLMs"),
            P(
                "I started working with Claude Sonnet 3.5, primarily because it's the "
                "latest model and Claudette makes it simple to use. The main mechanism, "
                "well-explained in the paper I mentioned earlier, involves prompting the "
                "model with a transcript containing speech attribution and asking it to "
                "identify and fix diarization mistakes."
            ),
            P(
                "I found that providing examples of common error types improved results. "
                "Here are some examples:"
            ),
            H4("Bleeding:"),
            Pre(
                Code(
                    "Speaker1: Hi my name is David. Hi my\nSpeaker2: name is David also"
                )
            ),
            H4("Burying:"),
            Pre(
                Code(
                    "Speaker1: Hi how are you? I'm fine, thanks! How are you? I'm doing well.\n"
                    "Speaker2: How's the weather over there?..."
                )
            ),
            P(
                "However, as with many LLM applications, context is crucial. Since we're "
                "primarily interested in diarizing long conversational content (10+ hours), "
                "we need to develop a strategy that acknowledges the limitations of the models "
                "we're using and finds ways to accommodate those limitations."
            ),
            P(
                "Firstly, it's cost-prohibitive to maximize the context for every interaction "
                "with the model. If your conversation has 1 million tokens and the model has a "
                "200k context window, by the time your back-and-forth reaches that window, the "
                "model's inference from that full context becomes much more expensive. Depending "
                "on your chosen chunk size, this could happen for another 40 interactions."
            ),
            P(
                "One solution is to reset the context occasionally while modifying the "
                "prompt to inform the model that it's processing mid-conversation data. That's "
                "the approach I took."
            ),
            P("You can explore my diarization with LLM package here:"),
            A(
                "github.com/russedavid/improve-diarization-with-llm",
                href="https://github.com/russedavid/improve-diarization-with-llm",
            ),
            P("And find the documentation here:"),
            A(
                "russedavid.github.io/improve-diarization-with-llm/",
                href="https://russedavid.github.io/improve-diarization-with-llm/",
            ),
        ),
    },
    "quick-diarization": {
        "title": "Quick and Easy Diarization: Step One in Building a Conversational Dataset",
        "date": "June 19, 2024",
        "snippet": "The full code for reference can be found here:",

        "content": Div(
            P("The full code for reference can be found here:"),
            A(
                "github.com/russedavid/diarization-stuff",
                href="https://github.com/russedavid/diarization-stuff",
            ),
            P(
                "I had an interesting idea recently about building a particular kind of "
                "conversational dataset, in a text format that could be used to fine-tune "
                "an LLM for a particular task. So I needed to figure out how to convert some "
                "audio I had into a text with diarization."
            ),
            P(
                "Diarization means, simply put, who said what. It converts a string of words "
                "into something like:"
            ),
            Pre(
                Code(
                    "Speaker 1: Oh what a lovely day.\nSpeaker 2: Oh what a lovely day, what a deal."
                )
            ),
            H3("Main software used:"),
            Ul(
                Li(
                    "WhisperX: An extension of the popular Whisper model tailored for more "
                    "complex speech processing tasks, including diarization."
                ),
                Li(
                    "FFmpeg: A powerful multimedia framework capable of handling various "
                    "audio formats and tasks, crucial for concatenating separate audio files into a single track."
                ),
                Li(
                    "Pyannote: A robust library for speaker diarization, which we integrate "
                    "through a model hosted on Hugging Face."
                ),
            ),
            H3("Workflow Overview"),
            P(
                "The process begins by preparing our environment and importing necessary "
                "libraries, setting up the device configuration to leverage GPU acceleration, "
                "and adjusting compute types for optimal memory management. If you're not using "
                "a CUDA-enabled GPU, you can adapt the settings to utilize a CPU."
            ),
            Pre(
                Code(
                    "import whisperx\nimport subprocess\n\n"
                    'device = "cuda"\n'
                    "batch_size = 16\n"
                    'compute_type = "float16"\n\n'
                    'model = whisperx.load_model("large-v2", device, compute_type=compute_type, language="en")'
                )
            ),
            H3("Audio Concatenation"),
            P(
                "If your dataset is like mine, then related audio may have been recorded over "
                "multiple sessions. Rather than process the sessions individually and lose out "
                "on the context of the whole related “conversation” for diarization purposes, I "
                "decided to concatenate them. Using the FFmpeg cli, we combine these into a single "
                "file, setting the stage for uniform processing, retaining the context of all sessions "
                "as the audio is diarized."
            ),
            Pre(
                Code(
                    "def concatenate_audios_ffmpeg(file_list, output_filename):\n"
                    '    with open("audio_list.txt", "w") as file:\n'
                    "        for audio_file in file_list:\n"
                    "            file.write(f\"file '{audio_file}'\\n\")\n"
                    '    command = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", "audio_list.txt", "-c", "copy", output_filename]\n'
                    "    subprocess.run(command, check=True)\n"
                    "    return whisperx.load_audio(output_filename)"
                )
            ),
            H3("Transcribing and Aligning Speech"),
            P(
                "Once the audio is prepared, we turn to WhisperX to transcribe the speech. "
                "Following transcription, we employ an alignment model to segment the speech, "
                "preparing it for diarization."
            ),
            P(
                "The diarization process identifies distinct speakers in the audio, tagging each "
                "segment appropriately. This is facilitated by the use of models that can handle "
                "the complexities of speaker change and overlapping speech seen in real-world scenarios."
            ),
        ),
    },
}