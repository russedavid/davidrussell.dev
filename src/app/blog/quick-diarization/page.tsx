import CodeBlock from "@/app/components/codeblock";

export default function Page() {
  return (
    <div className="blog-content">
      <h2 className="mb-2 text-xl font-semibold">
        Quick and Easy Diarization: Step One in Building a Conversational
        Dataset
      </h2>
      <div className="indent-4 opacity-60">June 19, 2024</div>
      <p>
        The full code for reference can be found here:
        <a href="https://github.com/russedavid/diarization-stuff/blob/main/diarize_audio.py">
          {" "}
          github.com/russedavid/diarization-stuff
        </a>
        <br />
        <br />I had an interesting idea recently about building a particular
        kind of conversational dataset, in a text format that could be used to
        fine-tune an LLM for a particular task. So I needed to figure out how to
        convert some audio I had into a text with diarization.
      </p>
      <p>
        Diarization means, simply put, who said what. It converts a string of
        words into something like:
      </p>
      <CodeBlock
        code={`
Speaker 1: Oh what a lovely day.
Speaker 2: Oh what a lovely day, what a deal.
        `}
      />
      <br />
      <br />
      <h3>Main software used:</h3>
      <br />
      <ul>
        <li>
          WhisperX: An extension of the popular Whisper model tailored for more
          complex speech processing tasks, including diarization.
        </li>
        <br />
        <li>
          FFmpeg: A powerful multimedia framework capable of handling various
          audio formats and tasks, crucial for concatenating separate audio
          files into a single track.
        </li>
        <br />
        <li>
          Pyannote: A robust library for speaker diarization, which we integrate
          through a model hosted on Hugging Face.
        </li>
      </ul>
      <br />
      <h3>Workflow Overview</h3>
      <p>
        The process begins by preparing our environment and importing necessary
        libraries, setting up the device configuration to leverage GPU
        acceleration, and adjusting compute types for optimal memory management.
        If you&apos;re not using a CUDA-enabled GPU, you can adapt the settings
        to utilize a CPU.
      </p>
      <CodeBlock
        code={`
import whisperx
import subprocess

device = "cuda"
batch_size = 16
compute_type = "float16"

model = whisperx.load_model("large-v2", device, compute_type=compute_type, language="en")
            `}
      />
      <br />
      <h3>Audio Concatenation</h3>
      <p>
        If your dataset is like mine, then related audio may have been recorded
        over multiple sessions. Rather than process the sessions individually
        and lose out on the context of the whole related “conversation” for
        diarization purposes, I decided to concatenate them. Using the FFmpeg
        cli, we combine these into a single file, setting the stage for uniform
        processing, retaining the context of all sessions as the audio is
        diarized.
      </p>
      <CodeBlock
        code={`
def concatenate_audios_ffmpeg(file_list, output_filename):
    with open("audio_list.txt", "w") as file:
        for audio_file in file_list:
            file.write(f"file '{audio_file}'\\n")
    command = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", "audio_list.txt", "-c", "copy", output_filename]
    subprocess.run(command, check=True)
    return whisperx.load_audio(output_filename)
      `}
      />

      <br />
      <h3>Transcribing and Aligning Speech</h3>
      <p>
        Once the audio is prepared, we turn to WhisperX to transcribe the
        speech. Following transcription, we employ an alignment model to segment
        the speech, preparing it for diarization.
      </p>
      <h3>Step 3: Speaker Diarization</h3>
      <p>
        The diarization process identifies distinct speakers in the audio,
        tagging each segment appropriately. This is facilitated by the Pyannote
        model. Speaking of which, you’ll need a Hugging Face account and to
        accept Pyannote’s conditions, in order to use the model.
      </p>
      <a href="https://huggingface.co/pyannote/speaker-diarization-3.1">
        huggingface.co/pyannote/speaker-diarization-3.1
      </a>
      <CodeBlock
        code={`
diarize_model = whisperx.DiarizationPipeline(model_name="pyannote/speaker-diarization-3.1", use_auth_token=hugging_face_api_key, device=device)
diarize_segments = diarize_model(audio)
result = whisperx.assign_word_speakers(diarize_segments, result)
              `}
      />
      <br />
      <h3>Structuring the Output</h3>
      <p>
        The final step organizes the transcription into a coherent format,
        grouping text by speakers, which makes it readable and theoretically
        more valuable as a dataset.
      </p>
      <h3>Conclusion</h3>
      <p>
        So, it’s that easy to start creating your own text data-set based on
        audio you have of conversations. But like I mentioned it’s not perfect,
        and you’ll probably want to enhance the dataset with the method in the
        next entry.
        <br />
        <br />
        Having said that, Google also just came out with context caching for
        Gemini 1.5, which could potentially be a great way to execute
        diarization with the full context of a long audio, so I may be exploring
        that in a future blog as well.
      </p>
      <p>Thanks for reading.</p>
    </div>
  );
}
